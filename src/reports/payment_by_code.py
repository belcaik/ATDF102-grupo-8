import sqlite3
from src.database import get_db_connection

def query_payment_by_code():
    print("\n--- Consultar Pago por Código ---")

    try:
        code = int(input("Ingrese el ID del pago a consultar: "))
    except ValueError:
        print("Error: El ID debe ser un número.")
        return

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM payments WHERE id = ?", (code,))

    payment = cursor.fetchone()

    conn.close()

    if payment:
        print("\nPago encontrado:")
        print(f"  ID: {payment['id']}")
        print(f"  Monto: ${payment['amount']}")
        print(f"  Descripción: {payment['description']}")

        print(f"  IDs Relacionados: Cliente {payment['id_client']} | Casa {payment['id_house']}")
    else:
        print(f"\nNo se encontró ningún pago con el ID '{code}'.")