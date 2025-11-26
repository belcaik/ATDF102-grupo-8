from src.modules.payment_type import create_payment_type, read_payment_types, update_payment_type, delete_payment_type

def list_payment_types():
    """Prints a list of all payment types from the database."""
    types = read_payment_types()

    if not types:
        print("No hay tipos de pago registrados.")
        return

    print("\n--- Listado de Tipos de Pago ---")
    for pt in types:
        print(f"ID: {pt.id} | Nombre: {pt.name}")
    print("-" * 30)


def add_payment_type():
    """Prompts for info and creates a new payment type in DB."""
    print("\n--- Agregar Nuevo Tipo de Pago ---")
    name = input("Ingrese nombre del tipo de pago (ej: Efectivo, Webpay): ")

    try:
        new_pt = create_payment_type(name)
        print(f"Tipo '{new_pt.name}' creado con éxito (ID: {new_pt.id}).")
    except Exception as e:
        print(f"Error al crear tipo de pago: {e}")

def edit_payment_type():
    """Prompts for ID and updates the payment type in DB."""
    list_payment_types()
    try:
        pt_id = int(input("\nIngrese el ID del tipo de pago a editar: "))
        name = input("Ingrese nuevo nombre: ")

        updated = update_payment_type(pt_id, name)

        if updated:
            print(f"Tipo '{updated.name}' actualizado con éxito.")
        else:
            print("Tipo de pago no encontrado.")

    except ValueError:
        print("Error: El ID debe ser un número.")


def remove_payment_type():
    """Prompts for ID and deletes from DB."""
    list_payment_types()
    try:
        pt_id = int(input("\nIngrese el ID del tipo de pago a eliminar: "))

        if delete_payment_type(pt_id):
            print("Tipo de pago eliminado con éxito.")
        else:
            print("Tipo de pago no encontrado.")

    except ValueError:
        print("Error: El ID debe ser un número.")


def payment_type_maintainer():
    """Shows the payment type maintainer menu."""

    while True:
        print("\n--- Mantenedor de Tipos de Pago ---")
        print("1. Listar tipos de pago")
        print("2. Agregar tipo de pago")
        print("3. Editar tipo de pago")
        print("4. Eliminar tipo de pago")
        print("5. Volver al menú principal")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            list_payment_types()
        elif choice == "2":
            add_payment_type()
        elif choice == "3":
            edit_payment_type()
        elif choice == "4":
            remove_payment_type()
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")