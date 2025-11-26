from dataclasses import dataclass
from typing import List, Optional
import sqlite3

from src.database import get_db_connection

@dataclass
class Commune:
    """Represents a local administrative division that groups condos."""
    id: int
    name: str
    region_id: int

def create_commune(name: str, region_id: int) -> Commune:
    """Creates a new commune in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO communes (name, region_id) VALUES (?, ?)", (name, region_id))
        conn.commit()

        new_id = cursor.lastrowid
        return Commune(id=new_id, name=name, region_id=region_id)

    except sqlite3.Error as e:
        print(f"Error creando comuna: {e}")
        conn.rollback()
        raise e
    finally:
        conn.close()

def read_communes() -> List[Commune]:
    """Returns the list of all communes from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM communes")
    rows = cursor.fetchall()
    conn.close()

    communes_list = []
    for row in rows:
        obj = Commune(
            id=row['id'],
            name=row['name'],
            region_id=row['region_id']
        )
        communes_list.append(obj)

    return communes_list


def update_commune(commune_id: int, name: str, region_id: int) -> Optional[Commune]:
    """Updates a commune's information in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
                       UPDATE communes
                       SET name      = ?,
                           region_id = ?
                       WHERE id = ?
                       ''', (name, region_id, commune_id))

        conn.commit()

        if cursor.rowcount > 0:
            return Commune(id=commune_id, name=name, region_id=region_id)
        else:
            return None

    except sqlite3.Error as e:
        print(f"Error actualizando comuna: {e}")
        return None
    finally:
        conn.close()


def delete_commune(commune_id: int) -> bool:
    """Deletes a commune from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM communes WHERE id = ?", (commune_id,))
        conn.commit()
        return cursor.rowcount > 0

    except sqlite3.Error as e:
        print(f"Error eliminando comuna: {e}")
        return False
    finally:
        conn.close()