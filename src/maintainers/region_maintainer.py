from src.modules.region import create_region, read_regions, update_region, delete_region

def list_regions():
    """Prints a list of all regions from the database."""
    regions = read_regions()

    if not regions:
        print("No hay regiones registradas.")
        return

    print("\n--- Listado de Regiones ---")
    for r in regions:
        print(f"ID: {r.id} | Nombre: {r.name}")
    print("-" * 30)


def add_region():
    """Prompts for info and creates a new region in DB."""
    print("\n--- Agregar Nueva Región ---")
    name = input("Ingrese nombre de la región: ")

    try:
        new_region = create_region(name)
        print(f"Región '{new_region.name}' creada con éxito (ID: {new_region.id}).")
    except Exception as e:
        print(f"Error al crear región: {e}")


def edit_region():
    """Prompts for ID and updates the region in DB."""
    list_regions()
    try:
        region_id = int(input("\nIngrese el ID de la región a editar: "))
        name = input("Ingrese nuevo nombre: ")

        updated = update_region(region_id, name)

        if updated:
            print(f"Región '{updated.name}' actualizada con éxito.")
        else:
            print("Región no encontrada.")

    except ValueError:
        print("Error: El ID debe ser un número.")


def remove_region():
    """Prompts for ID and deletes from DB."""
    list_regions()
    try:
        region_id = int(input("\nIngrese el ID de la región a eliminar: "))

        if delete_region(region_id):
            print("Región eliminada con éxito.")
        else:
            print("Región no encontrada.")

    except ValueError:
        print("Error: El ID debe ser un número.")


def region_maintainer():
    """Shows the region maintainer menu."""

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