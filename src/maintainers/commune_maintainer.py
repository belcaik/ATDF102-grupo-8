from modules.commune import create_commune, read_communes, update_commune, delete_commune

def list_communes():
    """Prints a list of all communes."""
    communes = read_communes()
    if not communes:
        print("No hay comunas registradas.")
        return
    for commune in communes:
        print(f"ID: {commune.id}, Nombre: {commune.name}, ID Región: {commune.region_id}")

def add_commune():
    """Prompts the user for commune information and creates a new commune."""
    name = input("Ingrese nombre de la comuna: ")
    region_id = int(input("Ingrese ID de la región: "))
    new_commune = create_commune(name, region_id)
    print(f"Comuna '{new_commune.name}' creada con éxito.")

def edit_commune():
    """Prompts the user for a commune ID and new information to update a commune."""
    list_communes()
    commune_id = int(input("Ingrese el ID de la comuna a editar: "))
    name = input("Ingrese nuevo nombre: ")
    region_id = int(input("Ingrese nuevo ID de la región: "))
    updated_commune = update_commune(commune_id, name, region_id)
    if updated_commune:
        print(f"Comuna '{updated_commune.name}' actualizada con éxito.")
    else:
        print("Comuna no encontrada.")

def remove_commune():
    """Prompts the user for a commune ID to delete a commune."""
    list_communes()
    commune_id = int(input("Ingrese el ID de la comuna a eliminar: "))
    if delete_commune(commune_id):
        print("Comuna eliminada con éxito.")
    else:
        print("Comuna no encontrada.")

def commune_maintainer():
    """Shows the commune maintainer menu and handles user input."""
    while True:
        print("\n--- Mantenedor de Comunas ---")
        print("1. Listar comunas")
        print("2. Agregar comuna")
        print("3. Editar comuna")
        print("4. Eliminar comuna")
        print("5. Volver al menú principal")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            list_communes()
        elif choice == "2":
            add_commune()
        elif choice == "3":
            edit_commune()
        elif choice == "4":
            remove_commune()
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
