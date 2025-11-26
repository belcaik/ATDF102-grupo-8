from dataclasses import dataclass
from typing import List, Optional
import sqlite3

from src.database import get_db_connection


@dataclass
class ClientType:
    """Represents a type of client (e.g., Propietario, Arrendatario)."""
    id: int
    name: str

def create_client_type(name: str) -> ClientType:
    """Creates a new client type in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO client_types (name) VALUES (?)", (name,))
        conn.commit()

        new_id = cursor.lastrowid
        return ClientType(id=new_id, name=name)

    except sqlite3.Error as e:
        print(f"Error creando tipo de cliente: {e}")
        conn.rollback()
        raise e
    finally:
        conn.close()

def read_client_types() -> List[ClientType]:
    """Returns the list of all client types from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM client_types")
    rows = cursor.fetchall()
    conn.close()

    types_list = []
    for row in rows:
        # row['name'] funciona gracias al row_factory en database.py
        obj = ClientType(id=row['id'], name=row['name'])
        types_list.append(obj)

    return types_list

def update_client_type(client_type_id: int, name: str) -> Optional[ClientType]:
    """Updates a client type's information in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
                       UPDATE client_types
                       SET name = ?
                       WHERE id = ?
                       ''', (name, client_type_id))

        conn.commit()

        if cursor.rowcount > 0:
            return ClientType(id=client_type_id, name=name)
        else:
            return None

    except sqlite3.Error as e:
        print(f"Error actualizando tipo de cliente: {e}")
        return None
    finally:
        conn.close()

def delete_client_type(client_type_id: int) -> bool:
    """Deletes a client type from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM client_types WHERE id = ?", (client_type_id,))
        conn.commit()

        return cursor.rowcount > 0

    except sqlite3.Error as e:
        print(f"Error eliminando tipo de cliente: {e}")
        return False
    finally:
        conn.close()