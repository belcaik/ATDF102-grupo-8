from modules.house import create_house, read_houses, update_house, delete_house

def list_houses():
    """Prints a list of all houses."""
    houses = read_houses()
    if not houses:
        print("No hay casas registradas.")
        return
    for house in houses:
        print(f"ID: {house.id}, Calle: {house.street}, Número: {house.number}, ID Tipo: {house.type_id}, ID Condominio: {house.condo_id}")

def add_house():
    """Prompts the user for house information and creates a new house."""
    street = input("Ingrese calle: ")
    number = input("Ingrese número: ")
    type_id = int(input("Ingrese ID del tipo de casa: "))
    condo_id = int(input("Ingrese ID del condominio: "))
    new_house = create_house(street, number, type_id, condo_id)
    print(f"Casa en '{new_house.street} {new_house.number}' creada con éxito.")

def edit_house():
    """Prompts the user for a house ID and new information to update a house."""
    list_houses()
    house_id = int(input("Ingrese el ID de la casa a editar: "))
    street = input("Ingrese nueva calle: ")
    number = input("Ingrese nuevo número: ")
    type_id = int(input("Ingrese nuevo ID del tipo de casa: "))
    condo_id = int(input("Ingrese nuevo ID del condominio: "))
    updated_house = update_house(house_id, street, number, type_id, condo_id)
    if updated_house:
        print(f"Casa en '{updated_house.street} {updated_house.number}' actualizada con éxito.")
    else:
        print("Casa no encontrada.")

def remove_house():
    """Prompts the user for a house ID to delete a house."""
    list_houses()
    house_id = int(input("Ingrese el ID de la casa a eliminar: "))
    if delete_house(house_id):
        print("Casa eliminada con éxito.")
    else:
        print("Casa no encontrada.")

def house_maintainer():
    """Shows the house maintainer menu and handles user input."""
    while True:
        print("\n--- Mantenedor de Casas ---")
        print("1. Listar casas")
        print("2. Agregar casa")
        print("3. Editar casa")
        print("4. Eliminar casa")
        print("5. Volver al menú principal")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            list_houses()
        elif choice == "2":
            add_house()
        elif choice == "3":
            edit_house()
        elif choice == "4":
            remove_house()
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
