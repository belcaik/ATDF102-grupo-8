
def total_paid_by_client_house(data):
    # Individual
    print("\nMonto total pagado por clientes con casa (individual):")
    for client in data["clients"]:
        total = sum(p.amount for p in data["payments"] 
                    if data["houses"][p.id_house - 1].client_id == client.id and \
                       data["houses"][p.id_house - 1].type_id == 1) # HouseType 'Casa' 
        if total > 0:
            print(f"  - {client.full_name}: ${total}")

    # Global
    global_total = sum(p.amount for p in data["payments"] if data["houses"][p.id_house - 1].type_id == 1)
    print(f"\nMonto total pagado por clientes con casa (global): ${global_total}")
