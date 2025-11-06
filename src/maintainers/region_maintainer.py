from modules.region import create_region, read_regions, update_region, delete_region

def list_regions():
    """Prints a list of all regions."""
    regions = read_regions()
    if not regions:
        print("No hay regiones registradas.")
        return
    for region in regions:
        print(f"ID: {region.id}, Nombre: {region.name}")

def add_region():
    """Prompts the user for region information and creates a new region."""
    name = input("Ingrese nombre de la región: ")
    new_region = create_region(name)
    print(f"Región '{new_region.name}' creada con éxito.")

def edit_region():
    """Prompts the user for a region ID and new information to update a region."""
    list_regions()
    region_id = int(input("Ingrese el ID de la región a editar: "))
    name = input("Ingrese nuevo nombre: ")
    updated_region = update_region(region_id, name)
    if updated_region:
        print(f"Región '{updated_region.name}' actualizada con éxito.")
    else:
        print("Región no encontrada.")

def remove_region():
    """Prompts the user for a region ID to delete a region."""
    list_regions()
    region_id = int(input("Ingrese el ID de la región a eliminar: "))
    if delete_region(region_id):
        print("Región eliminada con éxito.")
    else:
        print("Región no encontrada.")

def region_maintainer():
    """Shows the region maintainer menu and handles user input."""
    while True:
        print("\n--- Mantenedor de Regiones ---")
        print("1. Listar regiones")
        print("2. Agregar región")
        print("3. Editar región")
        print("4. Eliminar región")
        print("5. Volver al menú principal")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            list_regions()
        elif choice == "2":
            add_region()
        elif choice == "3":
            edit_region()
        elif choice == "4":
            remove_region()
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
