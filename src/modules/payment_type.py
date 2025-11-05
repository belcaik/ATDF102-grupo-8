from dataclasses import dataclass
from typing import List

@dataclass
class PaymentType:
    """Defines the payment method used for a transaction."""

    id: int
    name: str

payment_types: List[PaymentType] = []
next_payment_type_id = 1

def create_payment_type(name: str) -> PaymentType:
    """Creates a new payment type and adds it to the in-memory list."""
    global next_payment_type_id
    new_payment_type = PaymentType(id=next_payment_type_id, name=name)
    payment_types.append(new_payment_type)
    next_payment_type_id += 1
    return new_payment_type

def read_payment_types() -> List[PaymentType]:
    """Returns the list of all payment types."""
    return payment_types

def update_payment_type(payment_type_id: int, name: str) -> PaymentType | None:
    """Updates a payment type's information."""
    for payment_type in payment_types:
        if payment_type.id == payment_type_id:
            payment_type.name = name
            return payment_type
    return None

def delete_payment_type(payment_type_id: int) -> bool:
    """Deletes a payment type from the in-memory list."""
    global payment_types
    initial_len = len(payment_types)
    payment_types = [payment_type for payment_type in payment_types if payment_type.id != payment_type_id]
    return len(payment_types) < initial_len