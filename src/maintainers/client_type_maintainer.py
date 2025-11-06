

def list_client_types(client_types):
    """Prints a list of all client types."""
    if not client_types:
        print("No hay tipos de clientes registrados.")
        return
    for client_type in client_types:
        print(f"ID: {client_type.id}, Nombre: {client_type.name}")

def add_client_type(client_types):
    """Prompts the user for client type information and creates a new client type."""
    name = input("Ingrese nombre del tipo de cliente: ")
    new_client_type_id = max([ct.id for ct in client_types]) + 1
    new_client_type = {"id": new_client_type_id, "name": name}
    client_types.append(new_client_type)
    print(f"Tipo de cliente '{new_client_type['name']}' creado con éxito.")

def edit_client_type(client_types):
    """Prompts the user for a client type ID and new information to update a client type."""
    list_client_types(client_types)
    client_type_id = int(input("Ingrese el ID del tipo de cliente a editar: "))
    name = input("Ingrese nuevo nombre: ")
    for client_type in client_types:
        if client_type.id == client_type_id:
            client_type.name = name
            print(f"Tipo de cliente '{client_type.name}' actualizado con éxito.")
            return
    print("Tipo de cliente no encontrado.")

def remove_client_type(client_types):
    """Prompts the user for a client type ID to delete a client type."""
    list_client_types(client_types)
    client_type_id = int(input("Ingrese el ID del tipo de cliente a eliminar: "))
    initial_len = len(client_types)
    client_types[:] = [client_type for client_type in client_types if client_type.id != client_type_id]
    if len(client_types) < initial_len:
        print("Tipo de cliente eliminado con éxito.")
    else:
        print("Tipo de cliente no encontrado.")

def client_type_maintainer(data):
    """Shows the client type maintainer menu and handles user input."""
    while True:
        print("\n--- Mantenedor de Tipos de Cliente ---")
        print("1. Listar tipos de cliente")
        print("2. Agregar tipo de cliente")
        print("3. Editar tipo de cliente")
        print("4. Eliminar tipo de cliente")
        print("5. Volver al menú principal")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            list_client_types(data["client_types"])
        elif choice == "2":
            add_client_type(data["client_types"])
        elif choice == "3":
            edit_client_type(data["client_types"])
        elif choice == "4":
            remove_client_type(data["client_types"])
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
