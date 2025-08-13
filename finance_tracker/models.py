"""Data models for the finance tracker."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Literal


@dataclass
class Transaction:
    """Represents a single financial transaction.

    Attributes
    ----------
    amount:
        Monetary value of the transaction. Positive values are expected.
    category:
        Category associated with the transaction (e.g. "Food", "Rent").
    description:
        Optional human readable description of the transaction.
    date:
        Date when the transaction occurred. Defaults to today's date.
    type:
        Either ``"income"`` or ``"expense"``.
    """

    amount: float
    category: str
    description: str = ""
    date: date = field(default_factory=date.today)
    type: Literal["income", "expense"] = "expense"

    def normalized_amount(self) -> float:
        """Return the signed amount for balance calculations.

        Income is treated as positive and expenses as negative.
        """

        sign = 1 if self.type == "income" else -1
        return sign * self.amount
