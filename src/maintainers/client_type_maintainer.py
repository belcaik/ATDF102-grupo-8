from src.modules.client_type import create_client_type, read_client_types, update_client_type, delete_client_type


def list_client_types():
    """Prints a list of all client types from the database."""
    types = read_client_types()

    if not types:
        print("No hay tipos de clientes registrados.")
        return

    print("\n--- Listado de Tipos de Cliente ---")
    for ct in types:
        print(f"ID: {ct.id} | Nombre: {ct.name}")
    print("-" * 30)


def add_client_type():
    """Prompts the user for info and creates a new client type in DB."""
    print("\n--- Agregar Nuevo Tipo de Cliente ---")
    name = input("Ingrese nombre del tipo de cliente: ")

    try:
        new_type = create_client_type(name)
        print(f"Tipo '{new_type.name}' creado con éxito (ID: {new_type.id}).")
    except Exception as e:
        print(f"Error al crear: {e}")


def edit_client_type():
    """Prompts for ID and updates the client type in DB."""
    list_client_types()
    try:
        type_id = int(input("\nIngrese el ID del tipo a editar: "))
        name = input("Ingrese nuevo nombre: ")

        updated = update_client_type(type_id, name)

        if updated:
            print(f"Tipo '{updated.name}' actualizado con éxito.")
        else:
            print("Tipo no encontrado.")

    except ValueError:
        print("Error: El ID debe ser un número.")


def remove_client_type():
    """Prompts for ID and deletes from DB."""
    list_client_types()
    try:
        type_id = int(input("\nIngrese el ID del tipo a eliminar: "))

        if delete_client_type(type_id):
            print("Tipo eliminado con éxito.")
        else:
            print("Tipo no encontrado.")

    except ValueError:
        print("Error: El ID debe ser un número.")


def client_type_maintainer():
    """Shows the client type maintainer menu."""

    while True:
        print("\n--- Mantenedor de Tipos de Cliente ---")
        print("1. Listar tipos de cliente")
        print("2. Agregar tipo de cliente")
        print("3. Editar tipo de cliente")
        print("4. Eliminar tipo de cliente")
        print("5. Volver al menú principal")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            list_client_types()
        elif choice == "2":
            add_client_type()
        elif choice == "3":
            edit_client_type()
        elif choice == "4":
            remove_client_type()
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")