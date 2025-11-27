from dataclasses import dataclass
from typing import List, Optional
import sqlite3
from shared.database.db import get_db_connection



@dataclass
class Client:
    """Represents a client that can own or rent properties."""
    id: int
    rut: str
    full_name: str
    email: str
    phone: str

def create_client(rut: str, full_name: str, email: str, phone: str) -> Client:
    """Creates a new client in the SQLite database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
                       INSERT INTO clients (rut, full_name, email, phone)
                       VALUES (?, ?, ?, ?)
                       ''', (rut, full_name, email, phone))

        conn.commit()

        new_id = cursor.lastrowid

        return Client(id=new_id, rut=rut, full_name=full_name, email=email, phone=phone)

    except sqlite3.Error as e:
        print(f"Error al crear cliente: {e}")
        conn.rollback()
        raise e
    finally:
        conn.close()


def read_clients() -> List[Client]:
    """Returns the list of all clients from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clients")
    rows = cursor.fetchall()

    conn.close()

    clients_list = []
    for row in rows:
        client = Client(
            id=row['id'],
            rut=row['rut'],
            full_name=row['full_name'],
            email=row['email'],
            phone=row['phone']
        )
        clients_list.append(client)

    return clients_list


def update_client(client_id: int, rut: str, full_name: str, email: str, phone: str) -> Optional[Client]:
    """Updates a client's information in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
                       UPDATE clients
                       SET rut       = ?,
                           full_name = ?,
                           email     = ?,
                           phone     = ?
                       WHERE id = ?
                       ''', (rut, full_name, email, phone, client_id))

        conn.commit()

        if cursor.rowcount > 0:
            return Client(id=client_id, rut=rut, full_name=full_name, email=email, phone=phone)
        else:
            return None

    except sqlite3.Error as e:
        print(f"Error actualizando cliente: {e}")
        return None
    finally:
        conn.close()


def delete_client(client_id: int) -> bool:
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
        conn.commit()

        deleted = cursor.rowcount > 0
        return deleted

    except sqlite3.IntegrityError:
        print("Error: No se puede eliminar el cliente porque tiene propiedades o pagos asociados.")
        return False
    except sqlite3.Error as e:
        print(f"Error eliminando cliente: {e}")
        return False
    finally:
        conn.close()