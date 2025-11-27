import sys
from pathlib import Path

# Ensure project root is on sys.path so absolute imports like "src.reports" work when running as a script.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from menu.menu import main
from shared.database.db import inicializar_db

if __name__ == "__main__":
    print("--- Iniciando Sistema ---")

    inicializar_db()

    main()
