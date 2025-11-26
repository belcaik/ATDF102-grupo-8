from src.modules.payment_year import create_payment_year, read_payment_years, update_payment_year, delete_payment_year


def list_payment_years():
    """Prints a list of all payment years from the database."""
    years = read_payment_years()

    if not years:
        print("No hay años de pago registrados.")
        return

    print("\n--- Listado de Años de Pago ---")
    for py in years:
        print(f"ID: {py.id} | Año: {py.year}")
    print("-" * 30)


def add_payment_year():
    """Prompts for info and creates a new payment year in DB."""
    print("\n--- Agregar Nuevo Año de Pago ---")
    try:
        year = int(input("Ingrese año (ej: 2025): "))

        new_py = create_payment_year(year)
        print(f"Año '{new_py.year}' creado con éxito (ID: {new_py.id}).")

    except ValueError:
        print("Error: El año debe ser un número entero.")
    except Exception as e:
        print(f"Error al crear año: {e}")


def edit_payment_year():
    """Prompts for ID and updates the payment year in DB."""
    list_payment_years()
    try:
        py_id = int(input("\nIngrese el ID del año a editar: "))
        year = int(input("Ingrese nuevo año: "))

        updated = update_payment_year(py_id, year)

        if updated:
            print(f"Año '{updated.year}' actualizado con éxito.")
        else:
            print("Año de pago no encontrado.")

    except ValueError:
        print("Error: Los valores deben ser números enteros.")


def remove_payment_year():
    """Prompts for ID and deletes from DB."""
    list_payment_years()
    try:
        py_id = int(input("\nIngrese el ID del año a eliminar: "))

        if delete_payment_year(py_id):
            print("Año de pago eliminado con éxito.")
        else:
            print("Año de pago no encontrado.")

    except ValueError:
        print("Error: El ID debe ser un número.")


def payment_year_maintainer():
    """Shows the payment year maintainer menu."""

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