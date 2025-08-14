"""High level interface for managing budgets."""

from __future__ import annotations

from .budget import Budget
from .models import Transaction


class FinanceManager:
    """Facade providing convenient methods for common operations."""

    def __init__(self) -> None:
        self.budget = Budget()

    def add_income(self, amount: float, category: str = "General", description: str = "") -> None:
        """Record an income transaction."""

        tx = Transaction(amount=amount, category=category, description=description, type="income")
        self.budget.add_transaction(tx)

    def add_expense(self, amount: float, category: str = "General", description: str = "") -> None:
        """Record an expense transaction."""

        tx = Transaction(amount=amount, category=category, description=description, type="expense")
        self.budget.add_transaction(tx)

    def get_balance(self) -> float:
        """Return the current balance."""

        return self.budget.balance()

    def total_expenses_by_category(self, category: str) -> float:
        """Return the total expenses for a specific category."""

        return self.budget.total_by_category(category)

    def expenses_breakdown(self) -> dict[str, float]:
        """Return totals of expenses grouped by category."""

        return self.budget.totals_by_category()
