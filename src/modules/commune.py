from dataclasses import dataclass
from typing import List

@dataclass
class Commune:
    """Represents a local administrative division that groups condos."""

    id: int
    name: str
    region_id: int

communes: List[Commune] = []
next_commune_id = 1

def create_commune(name: str, region_id: int) -> Commune:
    """Creates a new commune and adds it to the in-memory list."""
    global next_commune_id
    new_commune = Commune(id=next_commune_id, name=name, region_id=region_id)
    communes.append(new_commune)
    next_commune_id += 1
    return new_commune

def read_communes() -> List[Commune]:
    """Returns the list of all communes."""
    return communes

def update_commune(commune_id: int, name: str, region_id: int) -> Commune | None:
    """Updates a commune's information."""
    for commune in communes:
        if commune.id == commune_id:
            commune.name = name
            commune.region_id = region_id
            return commune
    return None

def delete_commune(commune_id: int) -> bool:
    """Deletes a commune from the in-memory list."""
    global communes
    initial_len = len(communes)
    communes = [commune for commune in communes if commune.id != commune_id]
    return len(communes) < initial_len