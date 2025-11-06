

def list_payment_types(payment_types):
    """Prints a list of all payment types."""
    if not payment_types:
        print("No hay tipos de pago registrados.")
        return
    for payment_type in payment_types:
        print(f"ID: {payment_type.id}, Nombre: {payment_type.name}")

def add_payment_type(payment_types):
    """Prompts the user for payment type information and creates a new payment type."""
    name = input("Ingrese nombre del tipo de pago: ")
    new_payment_type_id = max([pt.id for pt in payment_types]) + 1
    new_payment_type = {"id": new_payment_type_id, "name": name}
    payment_types.append(new_payment_type)
    print(f"Tipo de pago '{new_payment_type['name']}' creado con éxito.")

def edit_payment_type(payment_types):
    """Prompts the user for a payment type ID and new information to update a payment type."""
    list_payment_types(payment_types)
    payment_type_id = int(input("Ingrese el ID del tipo de pago a editar: "))
    name = input("Ingrese nuevo nombre: ")
    for payment_type in payment_types:
        if payment_type.id == payment_type_id:
            payment_type.name = name
            print(f"Tipo de pago '{payment_type.name}' actualizado con éxito.")
            return
    print("Tipo de pago no encontrado.")

def remove_payment_type(payment_types):
    """Prompts the user for a payment type ID to delete a payment type."""
    list_payment_types(payment_types)
    payment_type_id = int(input("Ingrese el ID del tipo de pago a eliminar: "))
    initial_len = len(payment_types)
    payment_types[:] = [payment_type for payment_type in payment_types if payment_type.id != payment_type_id]
    if len(payment_types) < initial_len:
        print("Tipo de pago eliminado con éxito.")
    else:
        print("Tipo de pago no encontrado.")

def payment_type_maintainer(data):
    """Shows the payment type maintainer menu and handles user input."""
    while True:
        print("\n--- Mantenedor de Tipos de Pago ---")
        print("1. Listar tipos de pago")
        print("2. Agregar tipo de pago")
        print("3. Editar tipo de pago")
        print("4. Eliminar tipo de pago")
        print("5. Volver al menú principal")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            list_payment_types(data["payment_types"])
        elif choice == "2":
            add_payment_type(data["payment_types"])
        elif choice == "3":
            edit_payment_type(data["payment_types"])
        elif choice == "4":
            remove_payment_type(data["payment_types"])
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
