

def list_payments(payments):
    """Prints a list of all payments."""
    if not payments:
        print("No hay pagos registrados.")
        return
    for payment in payments:
        print(f"ID: {payment.id}, ID Cliente: {payment.id_client}, ID Casa: {payment.id_house}, ID Año: {payment.payment_year_id}, ID Mes: {payment.payment_month_id}, ID Tipo Pago: {payment.payment_type}, Monto: {payment.amount}, Descripción: {payment.description}")

def add_payment(payments):
    """Prompts the user for payment information and creates a new payment."""
    id_client = int(input("Ingrese ID del cliente: "))
    id_house = int(input("Ingrese ID de la casa: "))
    payment_year_id = int(input("Ingrese ID del año de pago: "))
    payment_month_id = int(input("Ingrese ID del mes de pago: "))
    payment_type = int(input("Ingrese ID del tipo de pago: "))
    amount = float(input("Ingrese monto: "))
    description = input("Ingrese descripción: ")
    new_payment_id = max([p.id for p in payments]) + 1
    new_payment = {"id": new_payment_id, "id_client": id_client, "id_house": id_house, "payment_year_id": payment_year_id, "payment_month_id": payment_month_id, "payment_type": payment_type, "amount": amount, "description": description}
    payments.append(new_payment)
    print(f"Pago de '{new_payment['amount']}' creado con éxito.")

def edit_payment(payments):
    """Prompts the user for a payment ID and new information to update a payment."""
    list_payments(payments)
    payment_id = int(input("Ingrese el ID del pago a editar: "))
    id_client = int(input("Ingrese nuevo ID del cliente: "))
    id_house = int(input("Ingrese nuevo ID de la casa: "))
    payment_year_id = int(input("Ingrese nuevo ID del año de pago: "))
    payment_month_id = int(input("Ingrese nuevo ID del mes de pago: "))
    payment_type = int(input("Ingrese nuevo ID del tipo de pago: "))
    amount = float(input("Ingrese nuevo monto: "))
    description = input("Ingrese nueva descripción: ")
    for payment in payments:
        if payment.id == payment_id:
            payment.id_client = id_client
            payment.id_house = id_house
            payment.payment_year_id = payment_year_id
            payment.payment_month_id = payment_month_id
            payment.payment_type = payment_type
            payment.amount = amount
            payment.description = description
            print(f"Pago de '{payment.amount}' actualizado con éxito.")
            return
    print("Pago no encontrado.")

def remove_payment(payments):
    """Prompts the user for a payment ID to delete a payment."""
    list_payments(payments)
    payment_id = int(input("Ingrese el ID del pago a eliminar: "))
    initial_len = len(payments)
    payments[:] = [payment for payment in payments if payment.id != payment_id]
    if len(payments) < initial_len:
        print("Pago eliminado con éxito.")
    else:
        print("Pago no encontrado.")

def payment_maintainer(data):
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
            list_payments(data["payments"])
        elif choice == "2":
            add_payment(data["payments"])
        elif choice == "3":
            edit_payment(data["payments"])
        elif choice == "4":
            remove_payment(data["payments"])
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
