"""
Configuración centralizada del sistema de logging.

Este módulo permite ajustar el comportamiento del logging sin modificar
código en múltiples lugares.
"""

import os
from pathlib import Path
from typing import Literal

# Directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parents[2]

# Configuración de logging
LOG_DIR = os.getenv("LOG_DIR", str(BASE_DIR / "logs"))
LOG_FILE = os.getenv("LOG_FILE", "app.log")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")  # TRACE, DEBUG, INFO, WARN, ERROR
CONSOLE_OUTPUT = os.getenv("CONSOLE_OUTPUT", "true").lower() in ("true", "1", "yes")

# Configuración por ambiente
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")  # development, staging, production

# Niveles recomendados por ambiente
ENV_LOG_LEVELS = {
    "development": "DEBUG",
    "staging": "INFO",
    "production": "WARN",
}


def get_log_level_for_env() -> str:
    """Retorna el nivel de log apropiado según el ambiente."""
    # Si está configurado explícitamente, respetarlo
    if os.getenv("LOG_LEVEL"):
        return LOG_LEVEL

    return ENV_LOG_LEVELS.get(ENVIRONMENT, "INFO")


# TODO: Configuración futura para output JSON (Grafana/Loki)
# JSON_OUTPUT = os.getenv("JSON_OUTPUT", "false").lower() in ("true", "1", "yes")
# LOKI_URL = os.getenv("LOKI_URL", None)
# GRAFANA_CLOUD_API_KEY = os.getenv("GRAFANA_CLOUD_API_KEY", None)
