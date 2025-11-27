from src.modules.commune import create_commune, read_communes, update_commune, delete_commune
from src.modules.region import read_regions


def list_communes():
    """Prints a list of all communes from the database."""
    communes = read_communes()

    if not communes:
        print("No hay comunas registradas.")
        return

    print("\n--- Listado de Comunas ---")
    for c in communes:
        print(f"ID: {c.id} | Comuna: {c.name} | ID Región: {c.region_id}")
    print("-" * 30)

def print_regions_helper():
    """Helper function to show available regions."""
    regions = read_regions()
    print("\n--- Regiones Disponibles ---")
    for r in regions:
        print(f"ID: {r.id} - {r.name}")
    print("----------------------------")


def add_commune():
    """Prompts for info and creates a new commune in DB."""
    print("\n--- Agregar Nueva Comuna ---")

    print_regions_helper()

    name = input("Ingrese nombre de la comuna: ")
    try:
        region_id = int(input("Ingrese ID de la región: "))
    except ValueError:
        print("Error: El ID de región debe ser un número.")
        return

    try:
        new_commune = create_commune(name, region_id)
        print(f"Comuna '{new_commune.name}' creada con éxito (ID: {new_commune.id}).")
    except ValueError as e:
        print(f"Error al crear comuna: {e}")
    except Exception as e:
        print(f"Error al crear comuna: {e}")

def edit_commune():
    """Prompts for ID and updates the commune in DB."""
    list_communes()
    try:
        commune_id = int(input("\nIngrese el ID de la comuna a editar: "))

        print_regions_helper()

        name = input("Ingrese nuevo nombre: ")
        region_id = int(input("Ingrese nuevo ID de la región: "))
    except ValueError:
        print("Error: Los IDs deben ser números.")
        return

    try:
        updated = update_commune(commune_id, name, region_id)

        if updated:
            print(f"Comuna '{updated.name}' actualizada con éxito.")
        else:
            print("Comuna no encontrada.")

    except ValueError as e:
        print(f"Error al actualizar comuna: {e}")


def remove_commune():
    """Prompts for ID and deletes from DB."""
    list_communes()
    try:
        commune_id = int(input("\nIngrese el ID de la comuna a eliminar: "))

        if delete_commune(commune_id):
            print("Comuna eliminada con éxito.")
        else:
            print("Comuna no encontrada.")

    except ValueError:
        print("Error: El ID debe ser un número.")


def commune_maintainer():
    """Shows the commune maintainer menu."""

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
