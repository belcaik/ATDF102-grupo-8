def total_collected_by_condo(data):
    # Individual
    print("Monto total recaudado por condominio (individual):")
    for condo in data["condos"]:
        total = sum(p.amount for p in data["payments"] if data["houses"][p.id_house - 1].condo_id == condo.id)
        print(f"  - {condo.name}: ${total}")

    # Global
    global_total = sum(p.amount for p in data["payments"])
    print(f"\nMonto total recaudado (global): ${global_total}")