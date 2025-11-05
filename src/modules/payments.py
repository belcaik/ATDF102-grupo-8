from dataclasses import dataclass
from typing import List

@dataclass
class Payments:
    """Stores billing information for a specific property and client."""

    id: int
    id_client: int
    id_house: int
    payment_year_id: int
    payment_month_id: int
    payment_type: int
    amount: float
    description: str

payments: List[Payments] = []
next_payment_id = 1

def create_payment(id_client: int, id_house: int, payment_year_id: int, payment_month_id: int, payment_type: int, amount: float, description: str) -> Payments:
    """Creates a new payment and adds it to the in-memory list."""
    global next_payment_id
    new_payment = Payments(id=next_payment_id, id_client=id_client, id_house=id_house, payment_year_id=payment_year_id, payment_month_id=payment_month_id, payment_type=payment_type, amount=amount, description=description)
    payments.append(new_payment)
    next_payment_id += 1
    return new_payment

def read_payments() -> List[Payments]:
    """Returns the list of all payments."""
    return payments

def update_payment(payment_id: int, id_client: int, id_house: int, payment_year_id: int, payment_month_id: int, payment_type: int, amount: float, description: str) -> Payments | None:
    """Updates a payment's information."""
    for payment in payments:
        if payment.id == payment_id:
            payment.id_client = id_client
            payment.id_house = id_house
            payment.payment_year_id = payment_year_id
            payment.payment_month_id = payment_month_id
            payment.payment_type = payment_type
            payment.amount = amount
            payment.description = description
            return payment
    return None

def delete_payment(payment_id: int) -> bool:
    """Deletes a payment from the in-memory list."""
    global payments
    initial_len = len(payments)
    payments = [payment for payment in payments if payment.id != payment_id]
    return len(payments) < initial_len