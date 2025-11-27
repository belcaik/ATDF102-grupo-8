from dataclasses import dataclass
from typing import List, Optional
import sqlite3

from shared.database.db import ensure_fk_exists, get_db_connection


@dataclass
class Payments:
    """Stores billing information for a specific property and client."""
    id: int
    id_client: int
    id_house: int
    payment_year_id: int
    payment_month_id: int
    payment_type: int
    amount: float
    description: str

def create_payment(id_client: int, id_house: int, payment_year_id: int,
                   payment_month_id: int, payment_type: int, amount: float,
                   description: str) -> Payments:
    """Creates a new payment in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        ensure_fk_exists(cursor, "clients", id_client)
        ensure_fk_exists(cursor, "houses", id_house)
        ensure_fk_exists(cursor, "payment_years", payment_year_id)
        ensure_fk_exists(cursor, "payment_months", payment_month_id)
        ensure_fk_exists(cursor, "payment_types", payment_type)
        sql = '''
              INSERT INTO payments
              (id_client, id_house, payment_year_id, payment_month_id, payment_type, amount, description)
              VALUES (?, ?, ?, ?, ?, ?, ?) \
              '''
        values = (id_client, id_house, payment_year_id, payment_month_id, payment_type, amount, description)

        cursor.execute(sql, values)
        conn.commit()

        new_id = cursor.lastrowid
        return Payments(
            id=new_id,
            id_client=id_client,
            id_house=id_house,
            payment_year_id=payment_year_id,
            payment_month_id=payment_month_id,
            payment_type=payment_type,
            amount=amount,
            description=description
        )

    except sqlite3.Error as e:
        print(f"Error registrando pago: {e}")
        conn.rollback()
        raise e
    finally:
        conn.close()


def read_payments() -> List[Payments]:
    """Returns the list of all payments from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM payments ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()

    payments_list = []
    for row in rows:
        obj = Payments(
            id=row['id'],
            id_client=row['id_client'],
            id_house=row['id_house'],
            payment_year_id=row['payment_year_id'],
            payment_month_id=row['payment_month_id'],
            payment_type=row['payment_type'],
            amount=row['amount'],
            description=row['description']
        )
        payments_list.append(obj)

    return payments_list

def update_payment(payment_id: int, id_client: int, id_house: int, payment_year_id: int,
                   payment_month_id: int, payment_type: int, amount: float,
                   description: str) -> Optional[Payments]:
    """Updates a payment's information in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        ensure_fk_exists(cursor, "clients", id_client)
        ensure_fk_exists(cursor, "houses", id_house)
        ensure_fk_exists(cursor, "payment_years", payment_year_id)
        ensure_fk_exists(cursor, "payment_months", payment_month_id)
        ensure_fk_exists(cursor, "payment_types", payment_type)
        sql = '''
              UPDATE payments
              SET id_client=?, \
                  id_house=?, \
                  payment_year_id=?, \
                  payment_month_id=?,
                  payment_type=?, \
                  amount=?, \
                  description=?
              WHERE id = ? \
              '''
        values = (id_client, id_house, payment_year_id, payment_month_id, payment_type, amount, description, payment_id)

        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount > 0:
            return Payments(
                id=payment_id,
                id_client=id_client,
                id_house=id_house,
                payment_year_id=payment_year_id,
                payment_month_id=payment_month_id,
                payment_type=payment_type,
                amount=amount,
                description=description
            )
        else:
            return None

    except sqlite3.Error as e:
        print(f"Error actualizando pago: {e}")
        return None
    finally:
        conn.close()


def delete_payment(payment_id: int) -> bool:
    """Deletes a payment from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM payments WHERE id = ?", (payment_id,))
        conn.commit()
        return cursor.rowcount > 0

    except sqlite3.Error as e:
        print(f"Error eliminando pago: {e}")
        return False
    finally:
        conn.close()
