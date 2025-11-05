from dataclasses import dataclass
from typing import List

@dataclass
class ClientType:
    """Represents a type of client."""

    id: int
    name: str

client_types: List[ClientType] = []
next_client_type_id = 1

def create_client_type(name: str) -> ClientType:
    """Creates a new client type and adds it to the in-memory list."""
    global next_client_type_id
    new_client_type = ClientType(id=next_client_type_id, name=name)
    client_types.append(new_client_type)
    next_client_type_id += 1
    return new_client_type

def read_client_types() -> List[ClientType]:
    """Returns the list of all client types."""
    return client_types

def update_client_type(client_type_id: int, name: str) -> ClientType | None:
    """Updates a client type's information."""
    for client_type in client_types:
        if client_type.id == client_type_id:
            client_type.name = name
            return client_type
    return None

def delete_client_type(client_type_id: int) -> bool:
    """Deletes a client type from the in-memory list."""
    global client_types
    initial_len = len(client_types)
    client_types = [client_type for client_type in client_types if client_type.id != client_type_id]
    return len(client_types) < initial_len