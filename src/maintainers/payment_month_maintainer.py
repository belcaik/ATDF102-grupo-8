from src.modules.payment_month import create_payment_month, read_payment_months, update_payment_month, delete_payment_month


def list_payment_months():
    """Prints a list of all payment months from the database."""
    months = read_payment_months()

    if not months:
        print("No hay meses de pago registrados.")
        return

    print("\n--- Listado de Meses de Pago ---")
    for pm in months:
        print(f"ID: {pm.id} | Nombre: {pm.name} ({pm.month_number})")
    print("-" * 30)


def add_payment_month():
    """Prompts for info and creates a new payment month in DB."""
    print("\n--- Agregar Nuevo Mes de Pago ---")
    name = input("Ingrese nombre del mes (ej: Enero): ")
    try:
        month_number = int(input("Ingrese número del mes (1-12): "))

        new_month = create_payment_month(name, month_number)
        print(f"Mes '{new_month.name}' creado con éxito (ID: {new_month.id}).")

    except ValueError:
        print("Error: El número del mes debe ser un entero.")
    except Exception as e:
        print(f"Error al crear mes: {e}")

def edit_payment_month():
    """Prompts for ID and updates the payment month in DB."""
    list_payment_months()
    try:
        pm_id = int(input("\nIngrese el ID del mes a editar: "))
        name = input("Ingrese nuevo nombre: ")
        month_number = int(input("Ingrese nuevo número del mes: "))

        updated = update_payment_month(pm_id, name, month_number)

        if updated:
            print(f"Mes '{updated.name}' actualizado con éxito.")
        else:
            print("Mes no encontrado.")

    except ValueError:
        print("Error: Los valores numéricos deben ser enteros.")


def remove_payment_month():
    """Prompts for ID and deletes from DB."""
    list_payment_months()
    try:
        pm_id = int(input("\nIngrese el ID del mes a eliminar: "))

        if delete_payment_month(pm_id):
            print("Mes eliminado con éxito.")
        else:
            print("Mes no encontrado.")

    except ValueError:
        print("Error: El ID debe ser un número.")


def payment_month_maintainer():
    """Shows the payment month maintainer menu."""

    while True:
        print("\n--- Mantenedor de Meses de Pago ---")
        print("1. Listar meses de pago")
        print("2. Agregar mes de pago")
        print("3. Editar mes de pago")
        print("4. Eliminar mes de pago")
        print("5. Volver al menú principal")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            list_payment_months()
        elif choice == "2":
            add_payment_month()
        elif choice == "3":
            edit_payment_month()
        elif choice == "4":
            remove_payment_month()
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")