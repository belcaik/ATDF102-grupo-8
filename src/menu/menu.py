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
    # Agrega aquí las opciones de reportes
    print("1. Volver al Menú Principal")

def main():
    while True:
        show_main_menu()
        choice = input("Seleccione una opción: ")

        if choice == "1":
            while True:
                show_maintainers_menu()
                sub_choice = input("Seleccione una opción: ")
                if sub_choice == "1":
                    from menu.client_maintainer import client_maintainer
                    client_maintainer()
                elif sub_choice == "2":
                    from menu.client_type_maintainer import client_type_maintainer
                    client_type_maintainer()
                elif sub_choice == "3":
                    from menu.commune_maintainer import commune_maintainer
                    commune_maintainer()
                elif sub_choice == "4":
                    from menu.condo_maintainer import condo_maintainer
                    condo_maintainer()
                elif sub_choice == "5":
                    from menu.house_type_maintainer import house_type_maintainer
                    house_type_maintainer()
                elif sub_choice == "6":
                    from menu.house_maintainer import house_maintainer
                    house_maintainer()
                elif sub_choice == "7":
                    from menu.payment_month_maintainer import payment_month_maintainer
                    payment_month_maintainer()
                elif sub_choice == "8":
                    from menu.payment_type_maintainer import payment_type_maintainer
                    payment_type_maintainer()
                elif sub_choice == "9":
                    from menu.payment_year_maintainer import payment_year_maintainer
                    payment_year_maintainer()
                elif sub_choice == "10":
                    from menu.payments_maintainer import payment_maintainer
                    payment_maintainer()
                elif sub_choice == "11":
                    from menu.region_maintainer import region_maintainer
                    region_maintainer()
                elif sub_choice == "12":
                    break
        elif choice == "2":
            while True:
                show_reports_menu()
                sub_choice = input("Seleccione una opción: ")
                if sub_choice == "1":
                    break
                # Aquí puedes agregar la lógica para cada opción del submenú de reportes
        elif choice == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
