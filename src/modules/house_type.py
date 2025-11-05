from dataclasses import dataclass
from typing import List

@dataclass
class HouseType:
    """Classifies a house according to its type (e.g., apartment, duplex)."""

    id: int
    name: str

house_types: List[HouseType] = []
next_house_type_id = 1

def create_house_type(name: str) -> HouseType:
    """Creates a new house type and adds it to the in-memory list."""
    global next_house_type_id
    new_house_type = HouseType(id=next_house_type_id, name=name)
    house_types.append(new_house_type)
    next_house_type_id += 1
    return new_house_type

def read_house_types() -> List[HouseType]:
    """Returns the list of all house types."""
    return house_types

def update_house_type(house_type_id: int, name: str) -> HouseType | None:
    """Updates a house type's information."""
    for house_type in house_types:
        if house_type.id == house_type_id:
            house_type.name = name
            return house_type
    return None

def delete_house_type(house_type_id: int) -> bool:
    """Deletes a house type from the in-memory list."""
    global house_types
    initial_len = len(house_types)
    house_types = [house_type for house_type in house_types if house_type.id != house_type_id]
    return len(house_types) < initial_len