

def list_condos(condos):
    """Prints a list of all condos."""
    if not condos:
        print("No hay condominios registrados.")
        return
    for condo in condos:
        print(f"ID: {condo.id}, Calle: {condo.street}, Número: {condo.number}, Nombre: {condo.name}, ID Comuna: {condo.commune_id}")

def add_condo(condos):
    """Prompts the user for condo information and creates a new condo."""
    street = input("Ingrese calle: ")
    number = input("Ingrese número: ")
    name = input("Ingrese nombre: ")
    commune_id = int(input("Ingrese ID de la comuna: "))
    new_condo_id = max([c.id for c in condos]) + 1
    new_condo = {"id": new_condo_id, "street": street, "number": number, "name": name, "commune_id": commune_id}
    condos.append(new_condo)
    print(f"Condominio '{new_condo['name']}' creado con éxito.")

def edit_condo(condos):
    """Prompts the user for a condo ID and new information to update a condo."""
    list_condos(condos)
    condo_id = int(input("Ingrese el ID del condominio a editar: "))
    street = input("Ingrese nueva calle: ")
    number = input("Ingrese nuevo número: ")
    name = input("Ingrese nuevo nombre: ")
    commune_id = int(input("Ingrese nuevo ID de la comuna: "))
    for condo in condos:
        if condo.id == condo_id:
            condo.street = street
            condo.number = number
            condo.name = name
            condo.commune_id = commune_id
            print(f"Condominio '{condo.name}' actualizado con éxito.")
            return
    print("Condominio no encontrado.")

def remove_condo(condos):
    """Prompts the user for a condo ID to delete a condo."""
    list_condos(condos)
    condo_id = int(input("Ingrese el ID del condominio a eliminar: "))
    initial_len = len(condos)
    condos[:] = [condo for condo in condos if condo.id != condo_id]
    if len(condos) < initial_len:
        print("Condominio eliminado con éxito.")
    else:
        print("Condominio no encontrado.")

def condo_maintainer(data):
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
            list_condos(data["condos"])
        elif choice == "2":
            add_condo(data["condos"])
        elif choice == "3":
            edit_condo(data["condos"])
        elif choice == "4":
            remove_condo(data["condos"])
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
