from dataclasses import dataclass
from typing import List, Optional
import sqlite3

from src.database import get_db_connection


@dataclass
class Region:
    """Represents a geographic region that contains multiple communes."""
    id: int
    name: str

def create_region(name: str) -> Region:
    """Creates a new region in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO regions (name) VALUES (?)", (name,))
        conn.commit()

        new_id = cursor.lastrowid
        return Region(id=new_id, name=name)

    except sqlite3.Error as e:
        print(f"Error creando región: {e}")
        conn.rollback()
        raise e
    finally:
        conn.close()


def read_regions() -> List[Region]:
    """Returns the list of all regions from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM regions")
    rows = cursor.fetchall()
    conn.close()

    regions_list = []
    for row in rows:
        obj = Region(id=row['id'], name=row['name'])
        regions_list.append(obj)

    return regions_list


def update_region(region_id: int, name: str) -> Optional[Region]:
    """Updates a region's information in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("UPDATE regions SET name = ? WHERE id = ?", (name, region_id))
        conn.commit()

        if cursor.rowcount > 0:
            return Region(id=region_id, name=name)
        else:
            return None

    except sqlite3.Error as e:
        print(f"Error actualizando región: {e}")
        return None
    finally:
        conn.close()

def delete_region(region_id: int) -> bool:
    """Deletes a region from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM regions WHERE id = ?", (region_id,))
        conn.commit()
        return cursor.rowcount > 0

    except sqlite3.Error as e:
        print(f"Error eliminando región: {e}")
        return False
    finally:
        conn.close()