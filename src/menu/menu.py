

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"  # Reset to default color

from mock_data import load_mock_data
from reports.payment_by_code import query_payment_by_code
from reports.payments_by_condo_month_year import list_payments_by_condo_month_year
from reports.total_collected_by_condo import total_collected_by_condo
from reports.total_paid_by_client_house import total_paid_by_client_house
from reports.total_paid_by_client_department import total_paid_by_client_department
from reports.total_collected_by_condo_month_year import total_collected_by_condo_month_year

def show_main_menu():
    print("Menú Principal")
    print("1. Mantenedores")
    print("2. Reportes")
    print("3. Salir")

def show_maintainers_menu():
    print("Submenú Mantenedores")
    print("1. Clientes")
    print("2. Tipos de Clientes")
    print("3. Comunas")
    print("4. Condominios")
    print("5. Tipos de Casas")
    print("6. Casas")
    print("7. Meses de Pago")
    print("8. Tipos de Pago")
    print("9. Años de Pago")
    print("10. Pagos")
    print("11. Regiones")
    print("12. Volver al Menú Principal")

def show_reports_menu():
    print("Submenú Reportes")
    print("1. Consultar pago de gastos comunes por código")
    print("2. Listar los pagos de gastos comunes por condominio, mes, año.")
    print("3. El monto total de dinero recaudado por los condominios (individual y global)")
    print("4. El monto total de dinero pagados por los clientes con casa (individual y global)")
    print("5. El monto total de dinero pagados por los clientes con departamento (individual y global)")
    print("6. El monto total de dinero recaudado por los condominios por mes y año (casa y departamento)")
    print("7. Volver al Menú Principal")

def main():
    data = load_mock_data()
    while True:
        show_main_menu()
        choice = input("Seleccione una opción: ")

        if choice == "1":
            while True:
                show_maintainers_menu()
                sub_choice = input("Seleccione una opción: ")
                if sub_choice == "1":
                    from maintainers.client_maintainer import client_maintainer
                    client_maintainer(data)
                elif sub_choice == "2":
                    from maintainers.client_type_maintainer import client_type_maintainer
                    client_type_maintainer(data)
                elif sub_choice == "3":
                    from maintainers.commune_maintainer import commune_maintainer
                    commune_maintainer(data)
                elif sub_choice == "4":
                    from maintainers.condo_maintainer import condo_maintainer
                    condo_maintainer(data)
                elif sub_choice == "5":
                    from maintainers.house_type_maintainer import house_type_maintainer
                    house_type_maintainer(data)
                elif sub_choice == "6":
                    from maintainers.house_maintainer import house_maintainer
                    house_maintainer(data)
                elif sub_choice == "7":
                    from maintainers.payment_month_maintainer import payment_month_maintainer
                    payment_month_maintainer(data)
                elif sub_choice == "8":
                    from maintainers.payment_type_maintainer import payment_type_maintainer
                    payment_type_maintainer(data)
                elif sub_choice == "9":
                    from maintainers.payment_year_maintainer import payment_year_maintainer
                    payment_year_maintainer(data)
                elif sub_choice == "10":
                    from maintainers.payments_maintainer import payment_maintainer
                    payment_maintainer(data)
                elif sub_choice == "11":
                    from maintainers.region_maintainer import region_maintainer
                    region_maintainer(data)
                elif sub_choice == "12":
                    break
                print("="*25)
                print("seleccione opcion valida\n")
                print("="*25)
        elif choice == "2":
            while True:
                show_reports_menu()
                sub_choice = input("Seleccione una opción: ")
                if sub_choice == "1":
                    query_payment_by_code(data)
                elif sub_choice == "2":
                    list_payments_by_condo_month_year(data)
                elif sub_choice == "3":
                    total_collected_by_condo(data)
                elif sub_choice == "4":
                    total_paid_by_client_house(data)
                elif sub_choice == "5":
                    total_paid_by_client_department(data)
                elif sub_choice == "6":
                    total_collected_by_condo_month_year(data)
                elif sub_choice == "7":
                    break
        elif choice == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
