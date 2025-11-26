import sqlite3
from src.database import get_db_connection


def total_paid_by_client_department():
    print("\n--- Reporte: Pagos de Clientes (Solo Departamentos) ---")

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        DEPTO_TYPE_ID = 2

        query_global = '''
                       SELECT SUM(p.amount)
                       FROM payments p
                                JOIN houses h ON p.id_house = h.id
                       WHERE h.type_id = ? \
                       '''
        cursor.execute(query_global, (DEPTO_TYPE_ID,))
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
                           ORDER BY total DESC \
                           '''

        cursor.execute(query_individual, (DEPTO_TYPE_ID,))
        rows = cursor.fetchall()

        print("\n[Detalle Individual]")
        if not rows:
            print("  No hay pagos registrados para departamentos.")

        for row in rows:
            print(f"  - {row['full_name']}: ${int(row['total'])}")

        print(f"\n[Resumen]")
        print(f" Monto total recaudado (Global Deptos): ${int(global_total)}")

    except Exception as e:
        print(f"Error en el reporte: {e}")
    finally:
        conn.close()