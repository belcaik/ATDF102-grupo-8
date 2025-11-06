

def list_communes(communes):
    """Prints a list of all communes."""
    if not communes:
        print("No hay comunas registradas.")
        return
    for commune in communes:
        print(f"ID: {commune.id}, Nombre: {commune.name}, ID Región: {commune.region_id}")

def add_commune(communes):
    """Prompts the user for commune information and creates a new commune."""
    name = input("Ingrese nombre de la comuna: ")
    region_id = int(input("Ingrese ID de la región: "))
    new_commune_id = max([c.id for c in communes]) + 1
    new_commune = {"id": new_commune_id, "name": name, "region_id": region_id}
    communes.append(new_commune)
    print(f"Comuna '{new_commune['name']}' creada con éxito.")

def edit_commune(communes):
    """Prompts the user for a commune ID and new information to update a commune."""
    list_communes(communes)
    commune_id = int(input("Ingrese el ID de la comuna a editar: "))
    name = input("Ingrese nuevo nombre: ")
    region_id = int(input("Ingrese nuevo ID de la región: "))
    for commune in communes:
        if commune.id == commune_id:
            commune.name = name
            commune.region_id = region_id
            print(f"Comuna '{commune.name}' actualizada con éxito.")
            return
    print("Comuna no encontrada.")

def remove_commune(communes):
    """Prompts the user for a commune ID to delete a commune."""
    list_communes(communes)
    commune_id = int(input("Ingrese el ID de la comuna a eliminar: "))
    initial_len = len(communes)
    communes[:] = [commune for commune in communes if commune.id != commune_id]
    if len(communes) < initial_len:
        print("Comuna eliminada con éxito.")
    else:
        print("Comuna no encontrada.")

def commune_maintainer(data):
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
            list_communes(data["communes"])
        elif choice == "2":
            add_commune(data["communes"])
        elif choice == "3":
            edit_commune(data["communes"])
        elif choice == "4":
            remove_commune(data["communes"])
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
