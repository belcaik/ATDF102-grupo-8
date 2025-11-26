from src.modules.condo import create_condo, read_condos, update_condo, delete_condo
from src.modules.commune import read_communes


def list_condos():
    """Prints a list of all condos from the database."""
    condos = read_condos()

    if not condos:
        print("No hay condominios registrados.")
        return

    print("\n--- Listado de Condominios ---")
    for c in condos:
        print(f"ID: {c.id} | Nombre: {c.name}")
        print(f"    Dirección: {c.street} #{c.number} | ID Comuna: {c.commune_id}")
    print("-" * 40)


def print_communes_helper():
    """Helper function to show available communes."""
    communes = read_communes()
    print("\n--- Comunas Disponibles ---")
    for c in communes:
        print(f"ID: {c.id} - {c.name}")
    print("---------------------------")


def add_condo():
    """Prompts for info and creates a new condo in DB."""
    print("\n--- Agregar Nuevo Condominio ---")

    street = input("Ingrese calle: ")
    number = input("Ingrese número: ")
    name = input("Ingrese nombre del condominio: ")

    # Ayuda visual para elegir comuna
    print_communes_helper()

    try:
        commune_id = int(input("Ingrese ID de la comuna: "))

        # Guardamos en DB
        new_condo = create_condo(street, number, name, commune_id)
        print(f"Condominio '{new_condo.name}' creado con éxito (ID: {new_condo.id}).")

    except ValueError:
        print("Error: El ID de la comuna debe ser un número.")
    except Exception as e:
        print(f"Error al crear condominio: {e}")


def edit_condo():
    """Prompts for ID and updates the condo in DB."""
    list_condos()
    try:
        condo_id = int(input("\nIngrese el ID del condominio a editar: "))

        street = input("Ingrese nueva calle: ")
        number = input("Ingrese nuevo número: ")
        name = input("Ingrese nuevo nombre: ")

        print_communes_helper()
        commune_id = int(input("Ingrese nuevo ID de la comuna: "))

        updated = update_condo(condo_id, street, number, name, commune_id)

        if updated:
            print(f"Condominio '{updated.name}' actualizado con éxito.")
        else:
            print("Condominio no encontrado.")

    except ValueError:
        print("Error: Los IDs deben ser números.")


def remove_condo():
    """Prompts for ID and deletes from DB."""
    list_condos()
    try:
        condo_id = int(input("\nIngrese el ID del condominio a eliminar: "))

        if delete_condo(condo_id):
            print("Condominio eliminado con éxito.")
        else:
            print("Condominio no encontrado.")

    except ValueError:
        print("Error: El ID debe ser un número.")


def condo_maintainer():
    """Shows the condo maintainer menu."""
    # Sin argumento 'data'

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