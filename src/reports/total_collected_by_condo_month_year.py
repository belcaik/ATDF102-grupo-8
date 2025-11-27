import sqlite3
from shared.database.db import get_db_connection


def total_collected_by_condo_month_year():
    print("\n--- Reporte: Recaudación por Condominio (Casa vs Depto) ---")

    try:
        month_id = int(input("Ingrese el ID del mes: "))
        year_id = int(input("Ingrese el ID del año: "))
    except ValueError:
        print("Error: Debe ingresar números válidos.")
        return

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        query = '''
                SELECT c.name, \
                       SUM(CASE WHEN h.type_id = 1 THEN p.amount ELSE 0 END) as total_casa, \
                       SUM(CASE WHEN h.type_id = 2 THEN p.amount ELSE 0 END) as total_depto
                FROM condos c
                         LEFT JOIN houses h ON c.id = h.condo_id
                         LEFT JOIN payments p ON h.id = p.id_house
                    AND p.payment_month_id = ?
                    AND p.payment_year_id = ?
                GROUP BY c.id, c.name \
                '''

        cursor.execute(query, (month_id, year_id))
        rows = cursor.fetchall()

        print(f"\nResumen para el Mes {month_id}/{year_id}:")

        if not rows:
            print("No se encontraron registros.")

        for row in rows:
            print(f"  - {row['name']}:")
            print(f"    - Casas:         ${int(row['total_casa'])}")
            print(f"    - Departamentos: ${int(row['total_depto'])}")

    except Exception as e:
        print(f"Error en el reporte: {e}")
    finally:
        conn.close()