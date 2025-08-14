import pytest

from finance_tracker.manager import FinanceManager


def test_balance_and_category_totals():
    manager = FinanceManager()
    manager.add_income(1000, "Salary")
    manager.add_expense(200, "Food")
    manager.add_expense(100, "Food")
    manager.add_expense(150, "Transport")

    assert manager.get_balance() == pytest.approx(550)
    assert manager.total_expenses_by_category("Food") == pytest.approx(300)

    breakdown = manager.expenses_breakdown()
    assert breakdown["Food"] == pytest.approx(300)
    assert breakdown["Transport"] == pytest.approx(150)
