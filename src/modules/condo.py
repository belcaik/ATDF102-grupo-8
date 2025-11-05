from dataclasses import dataclass
from typing import List

@dataclass
class Condo:
    """Represents a condo building that contains multiple houses."""

    id: int
    street: str
    number: str
    name: str
    commune_id: int

condos: List[Condo] = []
next_condo_id = 1

def create_condo(street: str, number: str, name: str, commune_id: int) -> Condo:
    """Creates a new condo and adds it to the in-memory list."""
    global next_condo_id
    new_condo = Condo(id=next_condo_id, street=street, number=number, name=name, commune_id=commune_id)
    condos.append(new_condo)
    next_condo_id += 1
    return new_condo

def read_condos() -> List[Condo]:
    """Returns the list of all condos."""
    return condos

def update_condo(condo_id: int, street: str, number: str, name: str, commune_id: int) -> Condo | None:
    """Updates a condo's information."""
    for condo in condos:
        if condo.id == condo_id:
            condo.street = street
            condo.number = number
            condo.name = name
            condo.commune_id = commune_id
            return condo
    return None

def delete_condo(condo_id: int) -> bool:
    """Deletes a condo from the in-memory list."""
    global condos
    initial_len = len(condos)
    condos = [condo for condo in condos if condo.id != condo_id]
    return len(condos) < initial_len