
def list_payments_by_condo_month_year(data):
    condo_id = int(input("Ingrese el ID del condominio: "))
    month_id = int(input("Ingrese el ID del mes: "))
    year_id = int(input("Ingrese el ID del año: "))

    payments = [p for p in data["payments"] 
                if data["houses"][p.id_house - 1].condo_id == condo_id and \
                   p.payment_month_id == month_id and \
                   p.payment_year_id == year_id]

    if payments:
        print("\nPagos encontrados:")
        for p in payments:
            print(f"  - Código: {p.id}, Monto: ${p.amount}")
    else:
        print("\nNo se encontraron pagos para los criterios seleccionados.")
