import sqlite3
from shared.database.db import get_db_connection

from src.modules.condo import read_condos
from src.modules.payment_month import read_payment_months
from src.modules.payment_year import read_payment_years


def list_payments_by_condo_month_year():
    print("\n--- Reporte: Pagos por Condominio, Mes y Año ---")

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        condo_id = int(input("Ingrese el ID del condominio: "))
        month_id = int(input("Ingrese el ID del mes: "))
        year_id = int(input("Ingrese el ID del año: "))

        query = '''
                SELECT p.id, p.amount, p.description
                FROM payments p
                         JOIN houses h ON p.id_house = h.id
                WHERE h.condo_id = ?
                  AND p.payment_month_id = ?
                  AND p.payment_year_id = ? \
                '''

        cursor.execute(query, (condo_id, month_id, year_id))
        payments = cursor.fetchall()

        if payments:
            print(f"\nSe encontraron {len(payments)} pagos:")
            for p in payments:
                print(f"  - Código: {p['id']} | Monto: ${p['amount']} | Desc: {p['description']}")
        else:
            print("\nNo se encontraron pagos para los criterios seleccionados.")

    except ValueError:
        print("Error: Debe ingresar números válidos.")
    except Exception as e:
        print(f"Error en el reporte: {e}")
    finally:
        conn.close()