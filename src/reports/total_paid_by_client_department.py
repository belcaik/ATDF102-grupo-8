def total_paid_by_client_department(data):
    # Individual
    print("\nMonto total pagado por clientes con departamento (individual):")
    for client in data["clients"]:
        total = sum(p.amount for p in data["payments"] 
                    if data["houses"][p.id_house - 1].client_id == client.id and \
                       data["houses"][p.id_house - 1].type_id == 2) # HouseType 'Departamento' 
        if total > 0:
            print(f"  - {client.full_name}: ${total}")

    # Global
    global_total = sum(p.amount for p in data["payments"] if data["houses"][p.id_house - 1].type_id == 2)
    print(f"\nMonto total pagado por clientes con departamento (global): ${global_total}")