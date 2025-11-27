from dataclasses import dataclass
from typing import List, Optional
import sqlite3

from shared.database.db import get_db_connection


@dataclass
class PaymentYear:
    """Represents a fiscal year for payments."""
    id: int
    year: int

def create_payment_year(year: int) -> PaymentYear:
    """Creates a new payment year in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO payment_years (year) VALUES (?)", (year,))
        conn.commit()

        new_id = cursor.lastrowid
        return PaymentYear(id=new_id, year=year)

    except sqlite3.Error as e:
        print(f"Error creando año de pago: {e}")
        conn.rollback()
        raise e
    finally:
        conn.close()


def read_payment_years() -> List[PaymentYear]:
    """Returns the list of all payment years from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM payment_years ORDER BY year DESC")
    rows = cursor.fetchall()
    conn.close()

    years_list = []
    for row in rows:
        obj = PaymentYear(id=row['id'], year=row['year'])
        years_list.append(obj)

    return years_list


def update_payment_year(payment_year_id: int, year: int) -> Optional[PaymentYear]:
    """Updates a payment year's information in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("UPDATE payment_years SET year = ? WHERE id = ?", (year, payment_year_id))
        conn.commit()

        if cursor.rowcount > 0:
            return PaymentYear(id=payment_year_id, year=year)
        else:
            return None

    except sqlite3.Error as e:
        print(f"Error actualizando año de pago: {e}")
        return None
    finally:
        conn.close()


def delete_payment_year(payment_year_id: int) -> bool:
    """Deletes a payment year from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM payment_years WHERE id = ?", (payment_year_id,))
        conn.commit()
        return cursor.rowcount > 0

    except sqlite3.Error as e:
        print(f"Error eliminando año de pago: {e}")
        return False
    finally:
        conn.close()