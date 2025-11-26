from src.modules.house_type import create_house_type, read_house_types, update_house_type, delete_house_type

def list_house_types():
    """Prints a list of all house types from the database."""
    types = read_house_types()

    if not types:
        print("No hay tipos de casas registrados.")
        return

    print("\n--- Listado de Tipos de Casa ---")
    for ht in types:
        print(f"ID: {ht.id} | Nombre: {ht.name}")
    print("-" * 30)

def add_house_type():
    """Prompts for info and creates a new house type in DB."""
    print("\n--- Agregar Nuevo Tipo de Casa ---")
    name = input("Ingrese nombre del tipo de casa: ")

    try:
        new_type = create_house_type(name)
        print(f"Tipo '{new_type.name}' creado con éxito (ID: {new_type.id}).")
    except Exception as e:
        print(f"Error al crear: {e}")


def edit_house_type():
    """Prompts for ID and updates the house type in DB."""
    list_house_types()
    try:
        type_id = int(input("\nIngrese el ID del tipo a editar: "))
        name = input("Ingrese nuevo nombre: ")

        updated = update_house_type(type_id, name)

        if updated:
            print(f"Tipo '{updated.name}' actualizado con éxito.")
        else:
            print("Tipo no encontrado.")

    except ValueError:
        print("Error: El ID debe ser un número.")


def remove_house_type():
    """Prompts for ID and deletes from DB."""
    list_house_types()
    try:
        type_id = int(input("\nIngrese el ID del tipo a eliminar: "))

        if delete_house_type(type_id):
            print("Tipo eliminado con éxito.")
        else:
            print("Tipo no encontrado.")

    except ValueError:
        print("Error: El ID debe ser un número.")


def house_type_maintainer():
    """Shows the house type maintainer menu."""

    while True:
        print("\n--- Mantenedor de Tipos de Casa ---")
        print("1. Listar tipos de casa")
        print("2. Agregar tipo de casa")
        print("3. Editar tipo de casa")
        print("4. Eliminar tipo de casa")
        print("5. Volver al menú principal")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            list_house_types()
        elif choice == "2":
            add_house_type()
        elif choice == "3":
            edit_house_type()
        elif choice == "4":
            remove_house_type()
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")