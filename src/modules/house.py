from dataclasses import dataclass
from typing import List, Optional
import sqlite3

from shared.database.db import ensure_fk_exists, get_db_connection


@dataclass
class House:
    """Represents an individual housing unit within a condo complex."""
    id: int
    street: str
    number: str
    type_id: int
    condo_id: int
    client_id: int

def create_house(street: str, number: str, type_id: int, condo_id: int, client_id: int) -> House:
    """Creates a new house in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        ensure_fk_exists(cursor, "house_types", type_id)
        ensure_fk_exists(cursor, "condos", condo_id)
        ensure_fk_exists(cursor, "clients", client_id)
        cursor.execute('''
                       INSERT INTO houses (street, number, type_id, condo_id, client_id)
                       VALUES (?, ?, ?, ?, ?)
                       ''', (street, number, type_id, condo_id, client_id))

        conn.commit()

        new_id = cursor.lastrowid
        return House(id=new_id, street=street, number=number, type_id=type_id, condo_id=condo_id, client_id=client_id)

    except sqlite3.Error as e:
        print(f"Error creando propiedad: {e}")
        conn.rollback()
        raise e
    finally:
        conn.close()


def read_houses() -> List[House]:
    """Returns the list of all houses from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM houses")
    rows = cursor.fetchall()
    conn.close()

    houses_list = []
    for row in rows:
        obj = House(
            id=row['id'],
            street=row['street'],
            number=row['number'],
            type_id=row['type_id'],
            condo_id=row['condo_id'],
            client_id=row['client_id']
        )
        houses_list.append(obj)

    return houses_list


def update_house(house_id: int, street: str, number: str, type_id: int, condo_id: int, client_id: int) -> Optional[
    House]:
    """Updates a house's information in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        ensure_fk_exists(cursor, "house_types", type_id)
        ensure_fk_exists(cursor, "condos", condo_id)
        ensure_fk_exists(cursor, "clients", client_id)
        cursor.execute('''
                       UPDATE houses
                       SET street    = ?,
                           number    = ?,
                           type_id   = ?,
                           condo_id  = ?,
                           client_id = ?
                       WHERE id = ?
                       ''', (street, number, type_id, condo_id, client_id, house_id))

        conn.commit()

        if cursor.rowcount > 0:
            return House(id=house_id, street=street, number=number, type_id=type_id, condo_id=condo_id,
                         client_id=client_id)
        else:
            return None

    except sqlite3.Error as e:
        print(f"Error actualizando propiedad: {e}")
        return None
    finally:
        conn.close()


def delete_house(house_id: int) -> bool:
    """Deletes a house from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM houses WHERE id = ?", (house_id,))
        conn.commit()
        return cursor.rowcount > 0

    except sqlite3.IntegrityError:
        print("Error: No se puede eliminar la propiedad porque tiene pagos asociados.")
        return False
    except sqlite3.Error as e:
        print(f"Error eliminando propiedad: {e}")
        return False
    finally:
        conn.close()
