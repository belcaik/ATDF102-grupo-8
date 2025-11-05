from dataclasses import dataclass, field
from typing import List

@dataclass
class Client:
    """Represents a client that can own or rent properties."""

    id: int
    rut: str
    full_name: str
    email: str
    phone: str

clients: List[Client] = []
next_client_id = 1

def create_client(rut: str, full_name: str, email: str, phone: str) -> Client:
    """Creates a new client and adds it to the in-memory list."""
    global next_client_id
    new_client = Client(id=next_client_id, rut=rut, full_name=full_name, email=email, phone=phone)
    clients.append(new_client)
    next_client_id += 1
    return new_client

def read_clients() -> List[Client]:
    """Returns the list of all clients."""
    return clients

def update_client(client_id: int, rut: str, full_name: str, email: str, phone: str) -> Client | None:
    """Updates a client's information."""
    for client in clients:
        if client.id == client_id:
            client.rut = rut
            client.full_name = full_name
            client.email = email
            client.phone = phone
            return client
    return None

def delete_client(client_id: int) -> bool:
    """Deletes a client from the in-memory list."""
    global clients
    initial_len = len(clients)
    clients = [client for client in clients if client.id != client_id]
    return len(clients) < initial_len