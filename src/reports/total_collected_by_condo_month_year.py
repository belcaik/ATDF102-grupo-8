import sqlite3
from typing import List

from shared.database.db import get_db_connection


def get_total_collected_by_condo_month_year(month_id: int, year_id: int) -> List[sqlite3.Row]:
    """Returns totals by condo separated by house vs department for a given month/year."""
    conn = get_db_connection()
    cursor = conn.cursor()

    query = '''
            SELECT c.name,
                   SUM(CASE WHEN h.type_id = 1 THEN p.amount ELSE 0 END) as total_casa,
                   SUM(CASE WHEN h.type_id = 2 THEN p.amount ELSE 0 END) as total_depto
            FROM condos c
                     LEFT JOIN houses h ON c.id = h.condo_id
                     LEFT JOIN payments p ON h.id = p.id_house
                AND p.payment_month_id = ?
                AND p.payment_year_id = ?
            GROUP BY c.id, c.name
            ORDER BY c.name
            '''

    cursor.execute(query, (month_id, year_id))
    rows = cursor.fetchall()
    conn.close()
    return rows


def total_collected_by_condo_month_year():
    """CLI wrapper that prompts for IDs and prints condo totals."""
    print("\n--- Reporte: Recaudación por Condominio (Casa vs Depto) ---")

    try:
        month_id = int(input("Ingrese el ID del mes: "))
        year_id = int(input("Ingrese el ID del año: "))
    except ValueError:
        print("Error: Debe ingresar números válidos.")
        return

    try:
        rows = get_total_collected_by_condo_month_year(month_id, year_id)

        print(f"\nResumen para el Mes {month_id}/{year_id}:")

        if not rows:
            print("No se encontraron registros.")

        for row in rows:
            print(f"  - {row['name']}:")
            print(f"    - Casas:         ${int(row['total_casa'])}")
            print(f"    - Departamentos: ${int(row['total_depto'])}")

    except Exception as e:
        print(f"Error en el reporte: {e}")
