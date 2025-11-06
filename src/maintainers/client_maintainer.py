

def list_clients(clients):
    """Prints a list of all clients."""
    if not clients:
        print("No hay clientes registrados.")
        return
    for client in clients:
        print(f"ID: {client.id}, RUT: {client.rut}, Nombre: {client.full_name}, Email: {client.email}, Teléfono: {client.phone}")

def add_client(clients):
    """Prompts the user for client information and creates a new client."""
    rut = input("Ingrese RUT: ")
    full_name = input("Ingrese nombre completo: ")
    email = input("Ingrese email: ")
    phone = input("Ingrese teléfono: ")
    new_client_id = max([client.id for client in clients]) + 1
    new_client = {"id": new_client_id, "rut": rut, "full_name": full_name, "email": email, "phone": phone}
    clients.append(new_client)
    print(f"Cliente '{new_client['full_name']}' creado con éxito.")

def edit_client(clients):
    """Prompts the user for a client ID and new information to update a client."""
    list_clients(clients)
    client_id = int(input("Ingrese el ID del cliente a editar: ") )
    rut = input("Ingrese nuevo RUT: ")
    full_name = input("Ingrese nuevo nombre completo: ")
    email = input("Ingrese nuevo email: ")
    phone = input("Ingrese nuevo teléfono: ")
    for client in clients:
        if client.id == client_id:
            client.rut = rut
            client.full_name = full_name
            client.email = email
            client.phone = phone
            print(f"Cliente '{client.full_name}' actualizado con éxito.")
            return
    print("Cliente no encontrado.")

def remove_client(clients):
    """Prompts the user for a client ID to delete a client."""
    list_clients(clients)
    client_id = int(input("Ingrese el ID del cliente a eliminar: "))
    initial_len = len(clients)
    clients[:] = [client for client in clients if client.id != client_id]
    if len(clients) < initial_len:
        print("Cliente eliminado con éxito.")
    else:
        print("Cliente no encontrado.")

def client_maintainer(data):
    """Shows the client maintainer menu and handles user input."""
    while True:
        print("\n--- Mantenedor de Clientes ---")
        print("1. Listar clientes")
        print("2. Agregar cliente")
        print("3. Editar cliente")
        print("4. Eliminar cliente")
        print("5. Volver al menú principal")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            list_clients(data["clients"])
        elif choice == "2":
            add_client(data["clients"])
        elif choice == "3":
            edit_client(data["clients"])
        elif choice == "4":
            remove_client(data["clients"])
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
