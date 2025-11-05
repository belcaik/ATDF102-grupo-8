from dataclasses import dataclass
from typing import List

@dataclass
class PaymentYear:
    """Represents the calendar year associated with a payment."""

    id: int
    year: int

payment_years: List[PaymentYear] = []
next_payment_year_id = 1

def create_payment_year(year: int) -> PaymentYear:
    """Creates a new payment year and adds it to the in-memory list."""
    global next_payment_year_id
    new_payment_year = PaymentYear(id=next_payment_year_id, year=year)
    payment_years.append(new_payment_year)
    next_payment_year_id += 1
    return new_payment_year

def read_payment_years() -> List[PaymentYear]:
    """Returns the list of all payment years."""
    return payment_years

def update_payment_year(payment_year_id: int, year: int) -> PaymentYear | None:
    """Updates a payment year's information."""
    for payment_year in payment_years:
        if payment_year.id == payment_year_id:
            payment_year.year = year
            return payment_year
    return None

def delete_payment_year(payment_year_id: int) -> bool:
    """Deletes a payment year from the in-memory list."""
    global payment_years
    initial_len = len(payment_years)
    payment_years = [payment_year for payment_year in payment_years if payment_year.id != payment_year_id]
    return len(payment_years) < initial_len