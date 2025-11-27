import sqlite3
from typing import List

from shared.database.db import get_db_connection


def get_payments_by_condo_month_year(condo_id: int, month_id: int, year_id: int) -> List[sqlite3.Row]:
    """Returns payments for a condo filtered by month and year."""
    conn = get_db_connection()
    cursor = conn.cursor()

    query = '''
            SELECT p.id, p.amount, p.description
            FROM payments p
                     JOIN houses h ON p.id_house = h.id
            WHERE h.condo_id = ?
              AND p.payment_month_id = ?
              AND p.payment_year_id = ?
            ORDER BY p.id DESC
            '''

    cursor.execute(query, (condo_id, month_id, year_id))
    payments = cursor.fetchall()
    conn.close()
    return payments


def list_payments_by_condo_month_year():
    """CLI wrapper that prompts for IDs and prints the payments."""
    print("\n--- Reporte: Pagos por Condominio, Mes y Año ---")

    try:
        condo_id = int(input("Ingrese el ID del condominio: "))
        month_id = int(input("Ingrese el ID del mes: "))
        year_id = int(input("Ingrese el ID del año: "))
    except ValueError:
        print("Error: Debe ingresar números válidos.")
        return

    try:
        payments = get_payments_by_condo_month_year(condo_id, month_id, year_id)

        if payments:
            print(f"\nSe encontraron {len(payments)} pagos:")
            for p in payments:
                print(f"  - Código: {p['id']} | Monto: ${p['amount']} | Desc: {p['description']}")
        else:
            print("\nNo se encontraron pagos para los criterios seleccionados.")

    except Exception as e:
        print(f"Error en el reporte: {e}")
