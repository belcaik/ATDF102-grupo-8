from modules.payment_year import create_payment_year, read_payment_years, update_payment_year, delete_payment_year

def list_payment_years():
    """Prints a list of all payment years."""
    payment_years = read_payment_years()
    if not payment_years:
        print("No hay años de pago registrados.")
        return
    for payment_year in payment_years:
        print(f"ID: {payment_year.id}, Año: {payment_year.year}")

def add_payment_year():
    """Prompts the user for payment year information and creates a new payment year."""
    year = int(input("Ingrese año: "))
    new_payment_year = create_payment_year(year)
    print(f"Año de pago '{new_payment_year.year}' creado con éxito.")

def edit_payment_year():
    """Prompts the user for a payment year ID and new information to update a payment year."""
    list_payment_years()
    payment_year_id = int(input("Ingrese el ID del año de pago a editar: "))
    year = int(input("Ingrese nuevo año: "))
    updated_payment_year = update_payment_year(payment_year_id, year)
    if updated_payment_year:
        print(f"Año de pago '{updated_payment_year.year}' actualizado con éxito.")
    else:
        print("Año de pago no encontrado.")

def remove_payment_year():
    """Prompts the user for a payment year ID to delete a payment year."""
    list_payment_years()
    payment_year_id = int(input("Ingrese el ID del año de pago a eliminar: "))
    if delete_payment_year(payment_year_id):
        print("Año de pago eliminado con éxito.")
    else:
        print("Año de pago no encontrado.")

def payment_year_maintainer():
    """Shows the payment year maintainer menu and handles user input."""
    while True:
        print("\n--- Mantenedor de Años de Pago ---")
        print("1. Listar años de pago")
        print("2. Agregar año de pago")
        print("3. Editar año de pago")
        print("4. Eliminar año de pago")
        print("5. Volver al menú principal")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            list_payment_years()
        elif choice == "2":
            add_payment_year()
        elif choice == "3":
            edit_payment_year()
        elif choice == "4":
            remove_payment_year()
        elif choice == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
