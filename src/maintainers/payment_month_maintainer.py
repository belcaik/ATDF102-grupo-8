from modules.payment_month import create_payment_month, read_payment_months, update_payment_month, delete_payment_month

def list_payment_months():
    """Prints a list of all payment months."""
    payment_months = read_payment_months()
    if not payment_months:
        print("No hay meses de pago registrados.")
        return
    for payment_month in payment_months:
        print(f"ID: {payment_month.id}, Nombre: {payment_month.name}, Número: {payment_month.month_number}")

def add_payment_month():
    """Prompts the user for payment month information and creates a new payment month."""
    name = input("Ingrese nombre del mes: ")
    month_number = int(input("Ingrese número del mes: "))
    new_payment_month = create_payment_month(name, month_number)
    print(f"Mes de pago '{new_payment_month.name}' creado con éxito.")

def edit_payment_month():
    """Prompts the user for a payment month ID and new information to update a payment month."""
    list_payment_months()
    payment_month_id = int(input("Ingrese el ID del mes de pago a editar: "))
    name = input("Ingrese nuevo nombre: ")
    month_number = int(input("Ingrese nuevo número del mes: "))
    updated_payment_month = update_payment_month(payment_month_id, name, month_number)
    if updated_payment_month:
        print(f"Mes de pago '{updated_payment_month.name}' actualizado con éxito.")
    else:
        print("Mes de pago no encontrado.")

def remove_payment_month():
    """Prompts the user for a payment month ID to delete a payment month."""
    list_payment_months()
    payment_month_id = int(input("Ingrese el ID del mes de pago a eliminar: "))
    if delete_payment_month(payment_month_id):
        print("Mes de pago eliminado con éxito.")
    else:
        print("Mes de pago no encontrado.")

def payment_month_maintainer():
    """Shows the payment month maintainer menu and handles user input."""
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
