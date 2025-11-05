from modules.condo import create_condo, read_condos, update_condo, delete_condo

def list_condos():
    """Prints a list of all condos."""
    condos = read_condos()
    if not condos:
        print("No hay condominios registrados.")
        return
    for condo in condos:
        print(f"ID: {condo.id}, Calle: {condo.street}, Número: {condo.number}, Nombre: {condo.name}, ID Comuna: {condo.commune_id}")

def add_condo():
    """Prompts the user for condo information and creates a new condo."""
    street = input("Ingrese calle: ")
    number = input("Ingrese número: ")
    name = input("Ingrese nombre: ")
    commune_id = int(input("Ingrese ID de la comuna: "))
    new_condo = create_condo(street, number, name, commune_id)
    print(f"Condominio '{new_condo.name}' creado con éxito.")

def edit_condo():
    """Prompts the user for a condo ID and new information to update a condo."""
    list_condos()
    condo_id = int(input("Ingrese el ID del condominio a editar: "))
    street = input("Ingrese nueva calle: ")
    number = input("Ingrese nuevo número: ")
    name = input("Ingrese nuevo nombre: ")
    commune_id = int(input("Ingrese nuevo ID de la comuna: "))
    updated_condo = update_condo(condo_id, street, number, name, commune_id)
    if updated_condo:
        print(f"Condominio '{updated_condo.name}' actualizado con éxito.")
    else:
        print("Condominio no encontrado.")

def remove_condo():
    """Prompts the user for a condo ID to delete a condo."""
    list_condos()
    condo_id = int(input("Ingrese el ID del condominio a eliminar: "))
    if delete_condo(condo_id):
        print("Condominio eliminado con éxito.")
    else:
        print("Condominio no encontrado.")

def condo_maintainer():
    """Shows the condo maintainer menu and handles user input."""
    while True:
        print("\n--- Mantenedor de Condominios ---")
        print("1. Listar condominios")
        print("2. Agregar condominio")
        print("3. Editar condominio")
        print("4. Eliminar condominio")
        print("5. Volver al menú principal")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            list_condos()
        elif choice == "2":
            add_condo()
        elif choice == "3":
            edit_condo()
        elif choice == "4":
            remove_condo()
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
