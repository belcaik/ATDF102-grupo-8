import sqlite3
from typing import Optional

from shared.database.db import get_db_connection


def get_payment_by_id(payment_id: int) -> Optional[sqlite3.Row]:
    """Returns a payment row by ID or None if it does not exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM payments WHERE id = ?", (payment_id,))
    payment = cursor.fetchone()
    conn.close()
    return payment


def query_payment_by_code():
    """CLI wrapper that asks for an ID and prints the payment info."""
    print("\n--- Consultar Pago por Código ---")

    try:
        code = int(input("Ingrese el ID del pago a consultar: "))
    except ValueError:
        print("Error: El ID debe ser un número.")
        return

    payment = get_payment_by_id(code)

    if payment:
        print("\nPago encontrado:")
        print(f"  ID: {payment['id']}")
        print(f"  Monto: ${payment['amount']}")
        print(f"  Descripción: {payment['description']}")

        print(f"  IDs Relacionados: Cliente {payment['id_client']} | Casa {payment['id_house']}")
    else:
        print(f"\nNo se encontró ningún pago con el ID '{code}'.")
