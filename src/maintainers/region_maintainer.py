

def list_regions(regions):
    """Prints a list of all regions."""
    if not regions:
        print("No hay regiones registradas.")
        return
    for region in regions:
        print(f"ID: {region.id}, Nombre: {region.name}")

def add_region(regions):
    """Prompts the user for region information and creates a new region."""
    name = input("Ingrese nombre de la región: ")
    new_region_id = max([r.id for r in regions]) + 1
    new_region = {"id": new_region_id, "name": name}
    regions.append(new_region)
    print(f"Región '{new_region['name']}' creada con éxito.")

def edit_region(regions):
    """Prompts the user for a region ID and new information to update a region."""
    list_regions(regions)
    region_id = int(input("Ingrese el ID de la región a editar: "))
    name = input("Ingrese nuevo nombre: ")
    for region in regions:
        if region.id == region_id:
            region.name = name
            print(f"Región '{region.name}' actualizada con éxito.")
            return
    print("Región no encontrada.")

def remove_region(regions):
    """Prompts the user for a region ID to delete a region."""
    list_regions(regions)
    region_id = int(input("Ingrese el ID de la región a eliminar: "))
    initial_len = len(regions)
    regions[:] = [region for region in regions if region.id != region_id]
    if len(regions) < initial_len:
        print("Región eliminada con éxito.")
    else:
        print("Región no encontrada.")

def region_maintainer(data):
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
            list_regions(data["regions"])
        elif choice == "2":
            add_region(data["regions"])
        elif choice == "3":
            edit_region(data["regions"])
        elif choice == "4":
            remove_region(data["regions"])
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
