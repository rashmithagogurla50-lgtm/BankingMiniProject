# This class stores one transaction

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Transaction:
    transaction_type: str
    amount: float
    balance_after: float
    date: str


def create_transaction(transaction_type, amount, balance):
    return Transaction(
        transaction_type,
        amount,
        balance,
        str(datetime.now())
    )
