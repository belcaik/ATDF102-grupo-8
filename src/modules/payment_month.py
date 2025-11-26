from dataclasses import dataclass
from typing import List, Optional
import sqlite3

from src.database import get_db_connection


@dataclass
class PaymentMonth:
    """Represents the calendar month associated with a payment."""
    id: int
    name: str
    month_number: int

def create_payment_month(name: str, month_number: int) -> PaymentMonth:
    """Creates a new payment month in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO payment_months (name, month_number) VALUES (?, ?)", (name, month_number))
        conn.commit()

        new_id = cursor.lastrowid
        return PaymentMonth(id=new_id, name=name, month_number=month_number)

    except sqlite3.Error as e:
        print(f"Error creando mes de pago: {e}")
        conn.rollback()
        raise e
    finally:
        conn.close()


def read_payment_months() -> List[PaymentMonth]:
    """Returns the list of all payment months from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM payment_months ORDER BY month_number ASC")
    rows = cursor.fetchall()
    conn.close()

    months_list = []
    for row in rows:
        obj = PaymentMonth(
            id=row['id'],
            name=row['name'],
            month_number=row['month_number']
        )
        months_list.append(obj)

    return months_list


def update_payment_month(payment_month_id: int, name: str, month_number: int) -> Optional[PaymentMonth]:
    """Updates a payment month's information in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
                       UPDATE payment_months
                       SET name         = ?,
                           month_number = ?
                       WHERE id = ?
                       ''', (name, month_number, payment_month_id))

        conn.commit()

        if cursor.rowcount > 0:
            return PaymentMonth(id=payment_month_id, name=name, month_number=month_number)
        else:
            return None

    except sqlite3.Error as e:
        print(f"Error actualizando mes de pago: {e}")
        return None
    finally:
        conn.close()


def delete_payment_month(payment_month_id: int) -> bool:
    """Deletes a payment month from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM payment_months WHERE id = ?", (payment_month_id,))
        conn.commit()
        return cursor.rowcount > 0

    except sqlite3.Error as e:
        print(f"Error eliminando mes de pago: {e}")
        return False
    finally:
        conn.close()