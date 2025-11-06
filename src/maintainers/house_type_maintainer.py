from modules.house_type import create_house_type, read_house_types, update_house_type, delete_house_type

def list_house_types():
    """Prints a list of all house types."""
    house_types = read_house_types()
    if not house_types:
        print("No hay tipos de casas registrados.")
        return
    for house_type in house_types:
        print(f"ID: {house_type.id}, Nombre: {house_type.name}")

def add_house_type():
    """Prompts the user for house type information and creates a new house type."""
    name = input("Ingrese nombre del tipo de casa: ")
    new_house_type = create_house_type(name)
    print(f"Tipo de casa '{new_house_type.name}' creado con éxito.")

def edit_house_type():
    """Prompts the user for a house type ID and new information to update a house type."""
    list_house_types()
    house_type_id = int(input("Ingrese el ID del tipo de casa a editar: "))
    name = input("Ingrese nuevo nombre: ")
    updated_house_type = update_house_type(house_type_id, name)
    if updated_house_type:
        print(f"Tipo de casa '{updated_house_type.name}' actualizado con éxito.")
    else:
        print("Tipo de casa no encontrado.")

def remove_house_type():
    """Prompts the user for a house type ID to delete a house type."""
    list_house_types()
    house_type_id = int(input("Ingrese el ID del tipo de casa a eliminar: "))
    if delete_house_type(house_type_id):
        print("Tipo de casa eliminado con éxito.")
    else:
        print("Tipo de casa no encontrado.")

def house_type_maintainer():
    """Shows the house type maintainer menu and handles user input."""
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
