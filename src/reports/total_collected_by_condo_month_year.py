
def total_collected_by_condo_month_year(data):
    month_id = int(input("Ingrese el ID del mes: "))
    year_id = int(input("Ingrese el ID del año: "))

    print(f"\nMonto total recaudado por condominio para el mes {month_id} del año {year_id}:")
    for condo in data["condos"]:
        total_casa = sum(p.amount for p in data["payments"] 
                         if data["houses"][p.id_house - 1].condo_id == condo.id and \
                            p.payment_month_id == month_id and \
                            p.payment_year_id == year_id and \
                            data["houses"][p.id_house - 1].type_id == 1) # Casa
        
        total_depto = sum(p.amount for p in data["payments"] 
                          if data["houses"][p.id_house - 1].condo_id == condo.id and \
                             p.payment_month_id == month_id and \
                             p.payment_year_id == year_id and \
                             data["houses"][p.id_house - 1].type_id == 2) # Departamento

        print(f"  - {condo.name}:")
        print(f"    - Casas: ${total_casa}")
        print(f"    - Departamentos: ${total_depto}")

