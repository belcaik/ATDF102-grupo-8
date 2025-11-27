from src.modules.house import create_house, read_houses, update_house, delete_house
from src.modules.house_type import read_house_types
from src.modules.condo import read_condos
from src.modules.client import read_clients
from shared.logger import get_logger

logger = get_logger("maintainers.houses")


def list_houses():
    """Prints a list of all houses from the database."""
    houses = read_houses()

    if not houses:
        print("No hay casas registradas.")
        return

    print("\n--- Listado de Propiedades ---")
    for h in houses:
        print(f"ID: {h.id} | Dir: {h.street} #{h.number}")
        print(f"    Tipo ID: {h.type_id} | Condo ID: {h.condo_id} | Cliente ID: {h.client_id}")
    print("-" * 40)

def print_dependencies():
    """Muestra listas breves de tipos, condominios y clientes para elegir."""

    print("\n[1] Tipos de Propiedad:")
    for t in read_house_types():
        print(f"   ID {t.id}: {t.name}")

    print("\n[2] Condominios:")
    for c in read_condos():
        print(f"   ID {c.id}: {c.name}")

    print("\n[3] Clientes:")
    for cl in read_clients():
        print(f"   ID {cl.id}: {cl.full_name}")
    print("-" * 30)


def add_house():
    """Prompts for info and creates a new house in DB."""
    logger.info("Iniciando registro de nueva propiedad")
    print("\n--- Agregar Nueva Propiedad ---")

    street = input("Ingrese calle: ")
    number = input("Ingrese número: ")

    print_dependencies()

    try:
        type_id = int(input("Ingrese ID del tipo de casa: "))
        condo_id = int(input("Ingrese ID del condominio: "))
        client_id = int(input("Ingrese ID del cliente dueño: "))
    except ValueError:
        logger.warn("Entrada inválida al crear propiedad")
        print("Error: Los IDs deben ser números.")
        return

    try:
        logger.debug("Creando propiedad", street=street, number=number, type_id=type_id, condo_id=condo_id, client_id=client_id)
        new_house = create_house(street, number, type_id, condo_id, client_id)
        logger.info("Propiedad creada exitosamente", house_id=new_house.id, address=f"{street} {number}", client_id=client_id)
        print(f"Casa en '{new_house.street} {new_house.number}' creada con éxito (ID: {new_house.id}).")
    except ValueError as e:
        logger.error("Error de validación al crear propiedad", error=str(e), client_id=client_id, condo_id=condo_id)
        print(f"Error al crear casa: {e}")
    except Exception as e:
        logger.error("Error inesperado al crear propiedad", error=str(e), exc_info=True)
        print(f"Error al crear casa: {e}")


def edit_house():
    """Prompts for ID and updates the house in DB."""
    list_houses()
    try:
        house_id = int(input("\nIngrese el ID de la casa a editar: "))

        street = input("Ingrese nueva calle: ")
        number = input("Ingrese nuevo número: ")

        print_dependencies()

        type_id = int(input("Ingrese nuevo ID del tipo de casa: "))
        condo_id = int(input("Ingrese nuevo ID del condominio: "))
        client_id = int(input("Ingrese nuevo ID del cliente: "))
    except ValueError:
        print("Error: Los IDs deben ser números.")
        return

    try:
        updated = update_house(house_id, street, number, type_id, condo_id, client_id)

        if updated:
            print(f"Casa actualizada con éxito.")
        else:
            print("Casa no encontrada.")

    except ValueError as e:
        print(f"Error al actualizar casa: {e}")


def remove_house():
    """Prompts for ID and deletes from DB."""
    list_houses()
    try:
        house_id = int(input("\nIngrese el ID de la casa a eliminar: "))

        if delete_house(house_id):
            print("Casa eliminada con éxito.")
        else:
            print("Casa no encontrada.")

    except ValueError:
        print("Error: El ID debe ser un número.")


def house_maintainer():
    """Shows the house maintainer menu."""
    # Sin argumento 'data'

    while True:
        print("\n--- Mantenedor de Casas ---")
        print("1. Listar casas")
        print("2. Agregar casa")
        print("3. Editar casa")
        print("4. Eliminar casa")
        print("5. Volver al menú principal")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            list_houses()
        elif choice == "2":
            add_house()
        elif choice == "3":
            edit_house()
        elif choice == "4":
            remove_house()
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
