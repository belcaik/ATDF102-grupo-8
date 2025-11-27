from dataclasses import dataclass
from typing import List, Optional
import sqlite3

from shared.database.db import get_db_connection


@dataclass
class HouseType:
    """Classifies a house according to its type (e.g., apartment, duplex)."""
    id: int
    name: str

def create_house_type(name: str) -> HouseType:
    """Creates a new house type in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO house_types (name) VALUES (?)", (name,))
        conn.commit()

        new_id = cursor.lastrowid
        return HouseType(id=new_id, name=name)

    except sqlite3.Error as e:
        print(f"Error creando tipo de propiedad: {e}")
        conn.rollback()
        raise e
    finally:
        conn.close()


def read_house_types() -> List[HouseType]:
    """Returns the list of all house types from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM house_types")
    rows = cursor.fetchall()
    conn.close()

    types_list = []
    for row in rows:
        obj = HouseType(id=row['id'], name=row['name'])
        types_list.append(obj)

    return types_list


def update_house_type(house_type_id: int, name: str) -> Optional[HouseType]:
    """Updates a house type's information in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("UPDATE house_types SET name = ? WHERE id = ?", (name, house_type_id))
        conn.commit()

        if cursor.rowcount > 0:
            return HouseType(id=house_type_id, name=name)
        else:
            return None

    except sqlite3.Error as e:
        print(f"Error actualizando tipo de propiedad: {e}")
        return None
    finally:
        conn.close()


def delete_house_type(house_type_id: int) -> bool:
    """Deletes a house type from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM house_types WHERE id = ?", (house_type_id,))
        conn.commit()
        return cursor.rowcount > 0

    except sqlite3.Error as e:
        print(f"Error eliminando tipo de propiedad: {e}")
        return False
    finally:
        conn.close()