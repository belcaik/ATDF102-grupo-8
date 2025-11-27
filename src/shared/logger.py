"""
Módulo de logging estructurado para el sistema de gestión de condominios.

Proporciona logging con formato key=value fácil de parsear por máquina
y legible para humanos en desarrollo.

Características:
- Timestamp ISO 8601 con milisegundos y zona horaria
- Niveles: TRACE, DEBUG, INFO, WARN, ERROR
- Contexto estructurado (key=value)
- IDs de correlación (trace_id, request_id)
- Información de proceso/thread
- Ubicación de código (archivo:línea)
- Output a archivo .log

TODO: Implementar salida JSON para integración con Grafana/Loki
"""

import logging
import os
import sys
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional
import inspect


# Niveles de logging personalizados
TRACE = 5
logging.addLevelName(TRACE, "TRACE")


class StructuredFormatter(logging.Formatter):
    """
    Formatter que genera logs estructurados en formato key=value.

    Formato de salida:
    timestamp level [logger] location message key1=value1 key2=value2 ...

    Ejemplo:
    2025-11-26T22:31:45.123-03:00 INFO [payments] payments.py:28 Pago registrado payment_id=42 amount=15000 client_id=1
    """

    def __init__(self):
        super().__init__()
        self.hostname = os.uname().nodename if hasattr(os, 'uname') else 'unknown'

    def format(self, record: logging.LogRecord) -> str:
        # 1. Timestamp ISO 8601 con milisegundos y zona horaria
        dt = datetime.fromtimestamp(record.created, tz=timezone.utc).astimezone()
        timestamp = dt.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + dt.strftime('%z')
        # Formato: 2025-11-26T22:31:45.123-0300
        if len(timestamp) > 0 and timestamp[-2] != ':':
            # Agregar : en zona horaria para formato ISO completo: -03:00
            timestamp = timestamp[:-2] + ':' + timestamp[-2:]

        # 2. Level
        level = record.levelname

        # 3. Logger / componente
        logger_name = record.name

        # 4. Ubicación de código (file:line)
        location = f"{record.filename}:{record.lineno}"
        if hasattr(record, 'funcName') and record.funcName:
            location = f"{record.filename}:{record.funcName}:{record.lineno}"

        # 5. IDs de correlación (si existen)
        correlation_ids = []
        if hasattr(record, 'trace_id'):
            correlation_ids.append(f"trace_id={record.trace_id}")
        if hasattr(record, 'request_id'):
            correlation_ids.append(f"request_id={record.request_id}")
        if hasattr(record, 'span_id'):
            correlation_ids.append(f"span_id={record.span_id}")

        correlation_str = " ".join(correlation_ids)
        if correlation_str:
            correlation_str = f"[{correlation_str}]"

        # 6. Thread/Process info
        thread_info = f"pid={os.getpid()} tid={threading.get_ident()}"

        # 7. Mensaje principal
        message = record.getMessage()

        # 8. Contexto estructurado (key=value)
        context_parts = []
        if hasattr(record, 'context') and isinstance(record.context, dict):
            for key, value in record.context.items():
                # Escapar valores con espacios
                if isinstance(value, str) and (' ' in value or '=' in value):
                    value = f'"{value}"'
                context_parts.append(f"{key}={value}")

        context_str = " ".join(context_parts)

        # Construir línea completa
        parts = [
            timestamp,
            level,
            f"[{logger_name}]",
            f"({location})",
        ]

        if correlation_str:
            parts.append(correlation_str)

        parts.append(f"({thread_info})")
        parts.append(message)

        if context_str:
            parts.append(context_str)

        # Agregar exception info si existe
        if record.exc_info:
            parts.append("\n" + self.formatException(record.exc_info))

        return " ".join(parts)


class StructuredLogger:
    """
    Logger estructurado con métodos convenientes para agregar contexto.

    Uso:
        logger = get_logger("payments")
        logger.info("Pago creado", payment_id=42, amount=15000)
        logger.error("Falló validación", client_id=5, error="Cliente no existe")
    """

    def __init__(self, logger: logging.Logger):
        self._logger = logger
        self._context: Dict[str, Any] = {}

    def with_context(self, **kwargs) -> 'StructuredLogger':
        """
        Crea un nuevo logger con contexto adicional.

        Útil para agregar contexto que se repite en múltiples logs:

        request_logger = logger.with_context(request_id="abc-123", user_id=42)
        request_logger.info("Procesando solicitud")
        request_logger.info("Solicitud completada")
        """
        new_logger = StructuredLogger(self._logger)
        new_logger._context = {**self._context, **kwargs}
        return new_logger

    def _log(self, level: int, msg: str, **context):
        """Método interno para logging con contexto."""
        # Merge context
        full_context = {**self._context, **context}

        # Crear LogRecord extra con contexto
        extra = {'context': full_context}

        # Obtener información del caller (no del wrapper) y usar stacklevel
        self._logger.log(level, msg, extra=extra, stacklevel=3)

    def trace(self, msg: str, **context):
        """Log nivel TRACE - Para debugging muy detallado."""
        self._log(TRACE, msg, **context)

    def debug(self, msg: str, **context):
        """Log nivel DEBUG - Para información de debugging."""
        self._log(logging.DEBUG, msg, **context)

    def info(self, msg: str, **context):
        """Log nivel INFO - Para eventos normales importantes."""
        self._log(logging.INFO, msg, **context)

    def warn(self, msg: str, **context):
        """Log nivel WARN - Para situaciones inusuales pero manejables."""
        self._log(logging.WARNING, msg, **context)

    def warning(self, msg: str, **context):
        """Alias para warn()."""
        self.warn(msg, **context)

    def error(self, msg: str, exc_info=False, **context):
        """Log nivel ERROR - Para errores que requieren atención."""
        if exc_info:
            self._logger.error(msg, exc_info=True, extra={'context': {**self._context, **context}})
        else:
            self._log(logging.ERROR, msg, **context)


# Configuración global del sistema de logging
_initialized = False
_loggers: Dict[str, StructuredLogger] = {}


def setup_logging(
    log_dir: str = "logs",
    log_file: str = "app.log",
    level: str = "INFO",
    console_output: bool = False
) -> None:
    """
    Configura el sistema de logging global.

    Args:
        log_dir: Directorio donde guardar los logs
        log_file: Nombre del archivo de log
        level: Nivel mínimo de logging (TRACE, DEBUG, INFO, WARN, ERROR)
        console_output: Si True, también imprime logs en consola (False por defecto para no interferir con CLI)

    Debe llamarse una vez al inicio de la aplicación.
    IMPORTANTE: En aplicaciones CLI, mantener console_output=False para no interferir con la interfaz de usuario.
    """
    global _initialized

    if _initialized:
        return

    # Crear directorio de logs si no existe
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)

    # Configurar nivel
    level_map = {
        'TRACE': TRACE,
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARN': logging.WARNING,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
    }
    log_level = level_map.get(level.upper(), logging.INFO)

    # Configurar root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    # Remover handlers existentes
    root_logger.handlers.clear()

    # File handler con formato estructurado
    file_handler = logging.FileHandler(
        log_path / log_file,
        encoding='utf-8'
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(StructuredFormatter())
    root_logger.addHandler(file_handler)

    # Console handler (opcional) - formato simplificado para dev
    if console_output:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)

        # Formato más simple para consola
        console_format = logging.Formatter(
            '%(levelname)-5s [%(name)s] %(message)s'
        )
        console_handler.setFormatter(console_format)
        root_logger.addHandler(console_handler)

    _initialized = True

    # Log de inicio
    logger = get_logger('system')
    logger.info("Sistema de logging inicializado", log_level=level, log_file=str(log_path / log_file))


def get_logger(name: str) -> StructuredLogger:
    """
    Obtiene un logger estructurado por nombre.

    Args:
        name: Nombre del componente/módulo (ej: "payments", "auth", "database")

    Returns:
        StructuredLogger configurado

    Ejemplo:
        logger = get_logger("payments")
        logger.info("Procesando pago", payment_id=123, amount=5000)
    """
    if name not in _loggers:
        # Asegurar que el sistema está inicializado
        if not _initialized:
            setup_logging()

        native_logger = logging.getLogger(name)
        _loggers[name] = StructuredLogger(native_logger)

    return _loggers[name]


# Conveniencia: loggers predefinidos para módulos comunes
def get_module_logger(module_file: str) -> StructuredLogger:
    """
    Crea un logger basado en el nombre del archivo del módulo.

    Uso en un módulo:
        logger = get_module_logger(__file__)

    Extraerá el nombre del archivo (sin .py) como nombre del logger.
    """
    module_name = Path(module_file).stem
    return get_logger(module_name)
