

def list_houses(houses):
    """Prints a list of all houses."""
    if not houses:
        print("No hay casas registradas.")
        return
    for house in houses:
        print(f"ID: {house.id}, Calle: {house.street}, Número: {house.number}, ID Tipo: {house.type_id}, ID Condominio: {house.condo_id}")

def add_house(houses):
    """Prompts the user for house information and creates a new house."""
    street = input("Ingrese calle: ")
    number = input("Ingrese número: ")
    type_id = int(input("Ingrese ID del tipo de casa: "))
    condo_id = int(input("Ingrese ID del condominio: "))
    client_id = int(input("Ingrese ID del cliente: "))
    new_house_id = max([h.id for h in houses]) + 1
    new_house = {"id": new_house_id, "street": street, "number": number, "type_id": type_id, "condo_id": condo_id, "client_id": client_id}
    houses.append(new_house)
    print(f"Casa en '{new_house['street']} {new_house['number']}' creada con éxito.")

def edit_house(houses):
    """Prompts the user for a house ID and new information to update a house."""
    list_houses(houses)
    house_id = int(input("Ingrese el ID de la casa a editar: "))
    street = input("Ingrese nueva calle: ")
    number = input("Ingrese nuevo número: ")
    type_id = int(input("Ingrese nuevo ID del tipo de casa: "))
    condo_id = int(input("Ingrese nuevo ID del condominio: "))
    client_id = int(input("Ingrese nuevo ID del cliente: "))
    for house in houses:
        if house.id == house_id:
            house.street = street
            house.number = number
            house.type_id = type_id
            house.condo_id = condo_id
            house.client_id = client_id
            print(f"Casa en '{house.street} {house.number}' actualizada con éxito.")
            return
    print("Casa no encontrada.")

def remove_house(houses):
    """Prompts the user for a house ID to delete a house."""
    list_houses(houses)
    house_id = int(input("Ingrese el ID de la casa a eliminar: "))
    initial_len = len(houses)
    houses[:] = [house for house in houses if house.id != house_id]
    if len(houses) < initial_len:
        print("Casa eliminada con éxito.")
    else:
        print("Casa no encontrada.")

def house_maintainer(data):
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
            list_houses(data["houses"])
        elif choice == "2":
            add_house(data["houses"])
        elif choice == "3":
            edit_house(data["houses"])
        elif choice == "4":
            remove_house(data["houses"])
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
