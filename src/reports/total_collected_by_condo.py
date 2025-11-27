import sqlite3
from shared.database.db import get_db_connection


def total_collected_by_condo():
    print("\n--- Reporte: Total Recaudado por Condominio ---")

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT SUM(amount) FROM payments")
        result = cursor.fetchone()[0]
        global_total = result if result else 0  # Si es None (sin pagos), ponemos 0

        query = '''
                SELECT c.name, COALESCE(SUM(p.amount), 0) as total
                FROM condos c
                         LEFT JOIN houses h ON c.id = h.condo_id
                         LEFT JOIN payments p ON h.id = p.id_house
                GROUP BY c.id, c.name \
                '''

        cursor.execute(query)
        rows = cursor.fetchall()

        print("\n[Detalle Individual]")
        for row in rows:
            print(f"  - {row['name']}: ${int(row['total'])}")

        print(f"\n[Resumen]")
        print(f"Monto total recaudado (Global): ${int(global_total)}")

    except Exception as e:
        print(f"Error en el reporte: {e}")
    finally:
        conn.close()