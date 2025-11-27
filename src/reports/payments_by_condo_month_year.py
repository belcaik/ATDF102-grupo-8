import sqlite3
from typing import List
import time

from shared.database.db import get_db_connection
from shared.logger import get_logger

logger = get_logger("reports.payments_by_condo")


def get_payments_by_condo_month_year(condo_id: int, month_id: int, year_id: int) -> List[sqlite3.Row]:
    """Returns payments for a condo filtered by month and year."""
    logger.info("Generando reporte de pagos por condominio", condo_id=condo_id, month_id=month_id, year_id=year_id)
    start_time = time.time()

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

    duration_ms = int((time.time() - start_time) * 1000)
    logger.info("Reporte de pagos generado", condo_id=condo_id, month_id=month_id, year_id=year_id,
                payments_count=len(payments), duration_ms=duration_ms)

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
