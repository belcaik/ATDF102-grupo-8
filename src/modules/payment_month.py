from dataclasses import dataclass
from typing import List

@dataclass
class PaymentMonth:
    """Represents the calendar month associated with a payment."""

    id: int
    name: str
    month_number: int

payment_months: List[PaymentMonth] = []
next_payment_month_id = 1

def create_payment_month(name: str, month_number: int) -> PaymentMonth:
    """Creates a new payment month and adds it to the in-memory list."""
    global next_payment_month_id
    new_payment_month = PaymentMonth(id=next_payment_month_id, name=name, month_number=month_number)
    payment_months.append(new_payment_month)
    next_payment_month_id += 1
    return new_payment_month

def read_payment_months() -> List[PaymentMonth]:
    """Returns the list of all payment months."""
    return payment_months

def update_payment_month(payment_month_id: int, name: str, month_number: int) -> PaymentMonth | None:
    """Updates a payment month's information."""
    for payment_month in payment_months:
        if payment_month.id == payment_month_id:
            payment_month.name = name
            payment_month.month_number = month_number
            return payment_month
    return None

def delete_payment_month(payment_month_id: int) -> bool:
    """Deletes a payment month from the in-memory list."""
    global payment_months
    initial_len = len(payment_months)
    payment_months = [payment_month for payment_month in payment_months if payment_month.id != payment_month_id]
    return len(payment_months) < initial_len