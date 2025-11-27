from src.modules.payments import create_payment, read_payments, update_payment, delete_payment

from src.modules.client import read_clients
from src.modules.house import read_houses
from src.modules.payment_year import read_payment_years
from src.modules.payment_month import read_payment_months
from src.modules.payment_type import read_payment_types
from shared.logger import get_logger

logger = get_logger("maintainers.payments")


def list_payments():
    """Prints a list of all payments from the database."""
    payments = read_payments()

    if not payments:
        print("No hay pagos registrados.")
        return

    print("\n--- Historial de Pagos ---")
    for p in payments:
        print(f"ID Pago: {p.id} | Monto: ${p.amount} | Desc: {p.description}")
        print(
            f"   Datos: Cliente {p.id_client} | Casa {p.id_house} | Fecha: Mes {p.payment_month_id}/{p.payment_year_id} | Tipo: {p.payment_type}")
        print("-" * 50)

def print_dependencies():
    """Muestra resúmenes de IDs disponibles para ayudar al usuario."""
    print("\n--- AYUDA DE IDs DISPONIBLES ---")

    print(f"\n[Clientes]")
    for c in read_clients():
        print(f"ID {c.id}: {c.full_name}")

    print(f"\n[Propiedades]")
    for h in read_houses():
        print(f"ID {h.id}: {h.street} #{h.number}")

    print(f"\n[Calendario]")
    years = [str(y.year) for y in read_payment_years()]
    print(f"Años IDs: {years}")

    print(f"\n[Tipos de Pago]")
    for pt in read_payment_types():
        print(f"ID {pt.id}: {pt.name}")

    print("-" * 30)


def add_payment():
    """Prompts for info and creates a new payment in DB."""
    logger.info("Iniciando registro de nuevo pago")
    print("\n--- Registrar Nuevo Pago ---")

    print_dependencies()

    try:
        id_client = int(input("Ingrese ID del cliente: "))
        id_house = int(input("Ingrese ID de la casa: "))

        print("\n--- IDs Meses: 1=Enero ... 12=Diciembre ---")
        payment_month_id = int(input("Ingrese ID del mes de pago: "))
        payment_year_id = int(input("Ingrese ID del año de pago: "))

        payment_type = int(input("Ingrese ID del tipo de pago: "))

        amount = float(input("Ingrese monto ($): "))
        description = input("Ingrese descripción (ej: Gasto común): ")
    except ValueError:
        logger.warn("Entrada inválida en registro de pago")
        print("Error: Los IDs y montos deben ser números.")
        return

    try:
        logger.debug("Creando pago", client_id=id_client, house_id=id_house, amount=amount)
        new_pay = create_payment(id_client, id_house, payment_year_id, payment_month_id, payment_type, amount,
                                 description)
        logger.info("Pago registrado exitosamente", payment_id=new_pay.id, amount=new_pay.amount, client_id=id_client)
        print(f"Pago de ${new_pay.amount} registrado con éxito (ID Pago: {new_pay.id}).")
    except ValueError as e:
        logger.error("Error de validación al registrar pago", error=str(e), client_id=id_client, house_id=id_house)
        print(f"Error al registrar pago: {e}")
    except Exception as e:
        logger.error("Error inesperado al registrar pago", error=str(e), exc_info=True)
        print(f"Error al registrar pago: {e}")


def edit_payment():
    """Prompts for ID and updates the payment in DB."""
    list_payments()
    try:
        payment_id = int(input("\nIngrese el ID del pago a editar: "))

        print_dependencies()

        print("\n--- Ingrese los Nuevos Datos ---")
        id_client = int(input("Nuevo ID Cliente: "))
        id_house = int(input("Nuevo ID Casa: "))
        payment_year_id = int(input("Nuevo ID Año: "))
        payment_month_id = int(input("Nuevo ID Mes: "))
        payment_type = int(input("Nuevo ID Tipo Pago: "))
        amount = float(input("Nuevo Monto: "))
        description = input("Nueva Descripción: ")
    except ValueError:
        print("Error: Los valores numéricos son inválidos.")
        return

    try:
        updated = update_payment(payment_id, id_client, id_house, payment_year_id, payment_month_id, payment_type,
                                 amount, description)

        if updated:
            print(f"Pago actualizado con éxito.")
        else:
            print("Pago no encontrado.")

    except ValueError as e:
        print(f"Error al actualizar pago: {e}")


def remove_payment():
    """Prompts for ID and deletes from DB."""
    list_payments()
    try:
        payment_id = int(input("\nIngrese el ID del pago a eliminar: "))

        logger.info("Intentando eliminar pago", payment_id=payment_id)
        if delete_payment(payment_id):
            logger.info("Pago eliminado exitosamente", payment_id=payment_id)
            print("Pago eliminado con éxito.")
        else:
            logger.warn("Intento de eliminar pago inexistente", payment_id=payment_id)
            print("Pago no encontrado.")

    except ValueError:
        logger.warn("ID inválido al intentar eliminar pago")
        print("Error: El ID debe ser un número.")


def payment_maintainer():
    """Shows the payment maintainer menu."""

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
