import sqlite3
from typing import List
import time

from shared.database.db import get_db_connection
from shared.logger import get_logger

logger = get_logger("reports.total_collected")


def get_total_collected_by_condo_month_year(month_id: int, year_id: int) -> List[sqlite3.Row]:
    """Returns totals by condo separated by house vs department for a given month/year."""
    logger.info("Generando reporte de recaudación por condominio", month_id=month_id, year_id=year_id)
    start_time = time.time()

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

    duration_ms = int((time.time() - start_time) * 1000)
    logger.info("Reporte generado", month_id=month_id, year_id=year_id, condos_count=len(rows), duration_ms=duration_ms)

    return rows


def total_collected_by_condo_month_year():
    """CLI wrapper that prompts for IDs and prints condo totals."""
    logger.debug("Iniciando interfaz CLI de reporte de recaudación")
    print("\n--- Reporte: Recaudación por Condominio (Casa vs Depto) ---")

    try:
        month_id = int(input("Ingrese el ID del mes: "))
        year_id = int(input("Ingrese el ID del año: "))
    except ValueError:
        logger.warn("Entrada inválida en reporte de recaudación")
        print("Error: Debe ingresar números válidos.")
        return

    try:
        rows = get_total_collected_by_condo_month_year(month_id, year_id)

        print(f"\nResumen para el Mes {month_id}/{year_id}:")

        if not rows:
            logger.info("Reporte sin resultados", month_id=month_id, year_id=year_id)
            print("No se encontraron registros.")

        for row in rows:
            print(f"  - {row['name']}:")
            print(f"    - Casas:         ${int(row['total_casa'])}")
            print(f"    - Departamentos: ${int(row['total_depto'])}")

        logger.debug("Reporte mostrado exitosamente", month_id=month_id, year_id=year_id)

    except Exception as e:
        logger.error("Error al generar reporte", month_id=month_id, year_id=year_id, error=str(e), exc_info=True)
        print(f"Error en el reporte: {e}")
