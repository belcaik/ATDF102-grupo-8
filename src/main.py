from menu.menu import main
from shared.database.db import inicializar_db

if __name__ == "__main__":
    print("--- Iniciando Sistema ---")

    inicializar_db()

    main()