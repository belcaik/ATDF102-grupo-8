from dataclasses import dataclass
from typing import List

@dataclass
class House:
    """Represents an individual housing unit within a condo complex."""

    id: int
    street: str
    number: str
    type_id: int
    condo_id: int

houses: List[House] = []
next_house_id = 1

def create_house(street: str, number: str, type_id: int, condo_id: int) -> House:
    """Creates a new house and adds it to the in-memory list."""
    global next_house_id
    new_house = House(id=next_house_id, street=street, number=number, type_id=type_id, condo_id=condo_id)
    houses.append(new_house)
    next_house_id += 1
    return new_house

def read_houses() -> List[House]:
    """Returns the list of all houses."""
    return houses

def update_house(house_id: int, street: str, number: str, type_id: int, condo_id: int) -> House | None:
    """Updates a house's information."""
    for house in houses:
        if house.id == house_id:
            house.street = street
            house.number = number
            house.type_id = type_id
            house.condo_id = condo_id
            return house
    return None

def delete_house(house_id: int) -> bool:
    """Deletes a house from the in-memory list."""
    global houses
    initial_len = len(houses)
    houses = [house for house in houses if house.id != house_id]
    return len(houses) < initial_len