import sys
from pathlib import Path

# Ensure project root is on sys.path so absolute imports like "src.reports" work when running as a script.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from menu.menu import main
from shared.database.db import inicializar_db
from shared.logger import setup_logging, get_logger
from shared.logging_config import LOG_DIR, LOG_FILE, get_log_level_for_env

if __name__ == "__main__":
    # Inicializar sistema de logging (sin salida a consola para no interferir con CLI)
    setup_logging(
        log_dir=LOG_DIR,
        log_file=LOG_FILE,
        level=get_log_level_for_env(),
        console_output=False  # CRÍTICO: No imprimir a consola en aplicación CLI
    )

    logger = get_logger("main")
    logger.info("Sistema iniciado", version="1.0.0")

    print("--- Iniciando Sistema ---")

    try:
        inicializar_db()
        logger.info("Base de datos inicializada")

        main()

        logger.info("Sistema finalizado correctamente")
    except KeyboardInterrupt:
        logger.info("Sistema interrumpido por usuario")
        print("\n\nSistema finalizado por el usuario.")
    except Exception as e:
        logger.error("Error fatal en sistema", error=str(e), exc_info=True)
        print(f"\n\nError fatal: {e}")
        sys.exit(1)
