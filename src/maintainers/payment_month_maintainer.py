

def list_payment_months(payment_months):
    """Prints a list of all payment months."""
    if not payment_months:
        print("No hay meses de pago registrados.")
        return
    for payment_month in payment_months:
        print(f"ID: {payment_month.id}, Nombre: {payment_month.name}, Número: {payment_month.month_number}")

def add_payment_month(payment_months):
    """Prompts the user for payment month information and creates a new payment month."""
    name = input("Ingrese nombre del mes: ")
    month_number = int(input("Ingrese número del mes: "))
    new_payment_month_id = max([pm.id for pm in payment_months]) + 1
    new_payment_month = {"id": new_payment_month_id, "name": name, "month_number": month_number}
    payment_months.append(new_payment_month)
    print(f"Mes de pago '{new_payment_month['name']}' creado con éxito.")

def edit_payment_month(payment_months):
    """Prompts the user for a payment month ID and new information to update a payment month."""
    list_payment_months(payment_months)
    payment_month_id = int(input("Ingrese el ID del mes de pago a editar: "))
    name = input("Ingrese nuevo nombre: ")
    month_number = int(input("Ingrese nuevo número del mes: "))
    for payment_month in payment_months:
        if payment_month.id == payment_month_id:
            payment_month.name = name
            payment_month.month_number = month_number
            print(f"Mes de pago '{payment_month.name}' actualizado con éxito.")
            return
    print("Mes de pago no encontrado.")

def remove_payment_month(payment_months):
    """Prompts the user for a payment month ID to delete a payment month."""
    list_payment_months(payment_months)
    payment_month_id = int(input("Ingrese el ID del mes de pago a eliminar: "))
    initial_len = len(payment_months)
    payment_months[:] = [payment_month for payment_month in payment_months if payment_month.id != payment_month_id]
    if len(payment_months) < initial_len:
        print("Mes de pago eliminado con éxito.")
    else:
        print("Mes de pago no encontrado.")

def payment_month_maintainer(data):
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
            list_payment_months(data["payment_months"])
        elif choice == "2":
            add_payment_month(data["payment_months"])
        elif choice == "3":
            edit_payment_month(data["payment_months"])
        elif choice == "4":
            remove_payment_month(data["payment_months"])
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
