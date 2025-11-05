from dataclasses import dataclass
from typing import List

@dataclass
class Region:
    """Represents a geographic region that contains multiple communes."""

    id: int
    name: str

regions: List[Region] = []
next_region_id = 1

def create_region(name: str) -> Region:
    """Creates a new region and adds it to the in-memory list."""
    global next_region_id
    new_region = Region(id=next_region_id, name=name)
    regions.append(new_region)
    next_region_id += 1
    return new_region

def read_regions() -> List[Region]:
    """Returns the list of all regions."""
    return regions

def update_region(region_id: int, name: str) -> Region | None:
    """Updates a region's information."""
    for region in regions:
        if region.id == region_id:
            region.name = name
            return region
    return None

def delete_region(region_id: int) -> bool:
    """Deletes a region from the in-memory list."""
    global regions
    initial_len = len(regions)
    regions = [region for region in regions if region.id != region_id]
    return len(regions) < initial_len