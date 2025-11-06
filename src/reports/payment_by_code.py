
def query_payment_by_code(data):
    code = int(input("Ingrese el ID del pago a consultar: "))
    payment = next((p for p in data["payments"] if p.id == code), None)

    if payment:
        print("\nPago encontrado:")
        print(f"  ID: {payment.id}")
        print(f"  Monto: ${payment.amount}")
        print(f"  Descripción: {payment.description}")
    else:
        print(f"\nNo se encontró ningún pago con el ID '{code}'.")
