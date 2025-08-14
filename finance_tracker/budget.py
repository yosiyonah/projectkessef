"""Budget management utilities."""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, List

from .models import Transaction


class Budget:
    """Container for transactions with helper methods."""

    def __init__(self) -> None:
        self.transactions: List[Transaction] = []

    def add_transaction(self, transaction: Transaction) -> None:
        """Record a new :class:`Transaction`."""

        self.transactions.append(transaction)

    def total_by_category(self, category: str) -> float:
        """Return the total spent for ``category``."""

        return sum(t.amount for t in self.transactions if t.category == category and t.type == "expense")

    def totals_by_category(self) -> Dict[str, float]:
        """Return a mapping of categories to total expense amounts."""

        totals: Dict[str, float] = defaultdict(float)
        for t in self.transactions:
            if t.type == "expense":
                totals[t.category] += t.amount
        return dict(totals)

    def balance(self) -> float:
        """Return the current balance (income minus expenses)."""

        return sum(t.normalized_amount() for t in self.transactions)
