from dataclasses import dataclass
from typing import List, Optional
import sqlite3

from shared.database.db import ensure_fk_exists, get_db_connection


@dataclass
class Condo:
    """Represents a condo building that contains multiple houses."""
    id: int
    street: str
    number: str
    name: str
    commune_id: int

def create_condo(street: str, number: str, name: str, commune_id: int) -> Condo:
    """Creates a new condo in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        ensure_fk_exists(cursor, "communes", commune_id)
        cursor.execute('''
                       INSERT INTO condos (street, number, name, commune_id)
                       VALUES (?, ?, ?, ?)
                       ''', (street, number, name, commune_id))

        conn.commit()

        new_id = cursor.lastrowid
        return Condo(id=new_id, street=street, number=number, name=name, commune_id=commune_id)

    except sqlite3.Error as e:
        print(f"Error creando condominio: {e}")
        conn.rollback()
        raise e
    finally:
        conn.close()


def read_condos() -> List[Condo]:
    """Returns the list of all condos from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM condos")
    rows = cursor.fetchall()
    conn.close()

    condos_list = []
    for row in rows:
        obj = Condo(
            id=row['id'],
            street=row['street'],
            number=row['number'],
            name=row['name'],
            commune_id=row['commune_id']
        )
        condos_list.append(obj)

    return condos_list


def update_condo(condo_id: int, street: str, number: str, name: str, commune_id: int) -> Optional[Condo]:
    """Updates a condo's information in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        ensure_fk_exists(cursor, "communes", commune_id)
        cursor.execute('''
                       UPDATE condos
                       SET street     = ?,
                           number     = ?,
                           name       = ?,
                           commune_id = ?
                       WHERE id = ?
                       ''', (street, number, name, commune_id, condo_id))

        conn.commit()

        if cursor.rowcount > 0:
            return Condo(id=condo_id, street=street, number=number, name=name, commune_id=commune_id)
        else:
            return None

    except sqlite3.Error as e:
        print(f"Error actualizando condominio: {e}")
        return None
    finally:
        conn.close()


def delete_condo(condo_id: int) -> bool:
    """Deletes a condo from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM condos WHERE id = ?", (condo_id,))
        conn.commit()
        return cursor.rowcount > 0

    except sqlite3.Error as e:
        print(f"Error eliminando condominio: {e}")
        return False
    finally:
        conn.close()
