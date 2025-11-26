from menu.menu import main
from database import inicializar_db

if __name__ == "__main__":
    print("--- Iniciando Sistema ---")

    inicializar_db()

    main()