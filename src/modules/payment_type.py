from dataclasses import dataclass
from typing import List, Optional
import sqlite3

from shared.database.db import get_db_connection


@dataclass
class PaymentType:
    """Defines the payment method used for a transaction (e.g. Cash, Credit Card)."""
    id: int
    name: str

def create_payment_type(name: str) -> PaymentType:
    """Creates a new payment type in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO payment_types (name) VALUES (?)", (name,))
        conn.commit()

        new_id = cursor.lastrowid
        return PaymentType(id=new_id, name=name)

    except sqlite3.Error as e:
        print(f"Error creando tipo de pago: {e}")
        conn.rollback()
        raise e
    finally:
        conn.close()


def read_payment_types() -> List[PaymentType]:
    """Returns the list of all payment types from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM payment_types")
    rows = cursor.fetchall()
    conn.close()

    types_list = []
    for row in rows:
        obj = PaymentType(id=row['id'], name=row['name'])
        types_list.append(obj)

    return types_list


def update_payment_type(payment_type_id: int, name: str) -> Optional[PaymentType]:
    """Updates a payment type's information in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("UPDATE payment_types SET name = ? WHERE id = ?", (name, payment_type_id))
        conn.commit()

        if cursor.rowcount > 0:
            return PaymentType(id=payment_type_id, name=name)
        else:
            return None

    except sqlite3.Error as e:
        print(f"Error actualizando tipo de pago: {e}")
        return None
    finally:
        conn.close()


def delete_payment_type(payment_type_id: int) -> bool:
    """Deletes a payment type from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM payment_types WHERE id = ?", (payment_type_id,))
        conn.commit()
        return cursor.rowcount > 0

    except sqlite3.Error as e:
        print(f"Error eliminando tipo de pago: {e}")
        return False
    finally:
        conn.close()