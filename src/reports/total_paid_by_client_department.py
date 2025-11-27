import sqlite3
from typing import List, Tuple

from shared.database.db import get_db_connection

DEPARTMENT_TYPE_ID = 2


def get_total_paid_by_client_department() -> Tuple[int, List[sqlite3.Row]]:
    """Returns global total and per-client totals for departments."""
    conn = get_db_connection()
    cursor = conn.cursor()

    query_global = '''
                   SELECT SUM(p.amount)
                   FROM payments p
                            JOIN houses h ON p.id_house = h.id
                   WHERE h.type_id = ?
                   '''
    cursor.execute(query_global, (DEPARTMENT_TYPE_ID,))
    result = cursor.fetchone()[0]
    global_total = result if result else 0

    query_individual = '''
                       SELECT c.full_name, SUM(p.amount) as total
                       FROM clients c
                                JOIN houses h ON c.id = h.client_id
                                JOIN payments p ON h.id = p.id_house
                       WHERE h.type_id = ?
                       GROUP BY c.id, c.full_name
                       HAVING total > 0
                       ORDER BY total DESC
                       '''

    cursor.execute(query_individual, (DEPARTMENT_TYPE_ID,))
    rows = cursor.fetchall()
    conn.close()
    return int(global_total), rows


def total_paid_by_client_department():
    """CLI wrapper that prints totals for department payments."""
    print("\n--- Reporte: Pagos de Clientes (Solo Departamentos) ---")

    try:
        global_total, rows = get_total_paid_by_client_department()

        print("\n[Detalle Individual]")
        if not rows:
            print("  No hay pagos registrados para departamentos.")

        for row in rows:
            print(f"  - {row['full_name']}: ${int(row['total'])}")

        print(f"\n[Resumen]")
        print(f" Monto total recaudado (Global Deptos): ${int(global_total)}")

    except Exception as e:
        print(f"Error en el reporte: {e}")
