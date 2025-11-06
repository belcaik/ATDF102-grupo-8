from modules.client import create_client, read_clients, update_client, delete_client

def list_clients():
    """Prints a list of all clients."""
    clients = read_clients()
    if not clients:
        print("No hay clientes registrados.")
        return
    for client in clients:
        print(f"ID: {client.id}, RUT: {client.rut}, Nombre: {client.full_name}, Email: {client.email}, Teléfono: {client.phone}")

def add_client():
    """Prompts the user for client information and creates a new client."""
    rut = input("Ingrese RUT: ")
    full_name = input("Ingrese nombre completo: ")
    email = input("Ingrese email: ")
    phone = input("Ingrese teléfono: ")
    new_client = create_client(rut, full_name, email, phone)
    print(f"Cliente '{new_client.full_name}' creado con éxito.")

def edit_client():
    """Prompts the user for a client ID and new information to update a client."""
    list_clients()
    client_id = int(input("Ingrese el ID del cliente a editar: ") )
    rut = input("Ingrese nuevo RUT: ")
    full_name = input("Ingrese nuevo nombre completo: ")
    email = input("Ingrese nuevo email: ")
    phone = input("Ingrese nuevo teléfono: ")
    updated_client = update_client(client_id, rut, full_name, email, phone)
    if updated_client:
        print(f"Cliente '{updated_client.full_name}' actualizado con éxito.")
    else:
        print("Cliente no encontrado.")

def remove_client():
    """Prompts the user for a client ID to delete a client."""
    list_clients()
    client_id = int(input("Ingrese el ID del cliente a eliminar: "))
    if delete_client(client_id):
        print("Cliente eliminado con éxito.")
    else:
        print("Cliente no encontrado.")

def client_maintainer():
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
            list_clients()
        elif choice == "2":
            add_client()
        elif choice == "3":
            edit_client()
        elif choice == "4":
            remove_client()
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
