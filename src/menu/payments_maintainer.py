from modules.payments import create_payment, read_payments, update_payment, delete_payment

def list_payments():
    """Prints a list of all payments."""
    payments = read_payments()
    if not payments:
        print("No hay pagos registrados.")
        return
    for payment in payments:
        print(f"ID: {payment.id}, ID Cliente: {payment.id_client}, ID Casa: {payment.id_house}, ID Año: {payment.payment_year_id}, ID Mes: {payment.payment_month_id}, ID Tipo Pago: {payment.payment_type}, Monto: {payment.amount}, Descripción: {payment.description}")

def add_payment():
    """Prompts the user for payment information and creates a new payment."""
    id_client = int(input("Ingrese ID del cliente: "))
    id_house = int(input("Ingrese ID de la casa: "))
    payment_year_id = int(input("Ingrese ID del año de pago: "))
    payment_month_id = int(input("Ingrese ID del mes de pago: "))
    payment_type = int(input("Ingrese ID del tipo de pago: "))
    amount = float(input("Ingrese monto: "))
    description = input("Ingrese descripción: ")
    new_payment = create_payment(id_client, id_house, payment_year_id, payment_month_id, payment_type, amount, description)
    print(f"Pago de '{new_payment.amount}' creado con éxito.")

def edit_payment():
    """Prompts the user for a payment ID and new information to update a payment."""
    list_payments()
    payment_id = int(input("Ingrese el ID del pago a editar: "))
    id_client = int(input("Ingrese nuevo ID del cliente: "))
    id_house = int(input("Ingrese nuevo ID de la casa: "))
    payment_year_id = int(input("Ingrese nuevo ID del año de pago: "))
    payment_month_id = int(input("Ingrese nuevo ID del mes de pago: "))
    payment_type = int(input("Ingrese nuevo ID del tipo de pago: "))
    amount = float(input("Ingrese nuevo monto: "))
    description = input("Ingrese nueva descripción: ")
    updated_payment = update_payment(payment_id, id_client, id_house, payment_year_id, payment_month_id, payment_type, amount, description)
    if updated_payment:
        print(f"Pago de '{updated_payment.amount}' actualizado con éxito.")
    else:
        print("Pago no encontrado.")

def remove_payment():
    """Prompts the user for a payment ID to delete a payment."""
    list_payments()
    payment_id = int(input("Ingrese el ID del pago a eliminar: "))
    if delete_payment(payment_id):
        print("Pago eliminado con éxito.")
    else:
        print("Pago no encontrado.")

def payment_maintainer():
    """Shows the payment maintainer menu and handles user input."""
    while True:
        print("\n--- Mantenedor de Pagos ---")
        print("1. Listar pagos")
        print("2. Agregar pago")
        print("3. Editar pago")
        print("4. Eliminar pago")
        print("5. Volver al menú principal")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            list_payments()
        elif choice == "2":
            add_payment()
        elif choice == "3":
            edit_payment()
        elif choice == "4":
            remove_payment()
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
