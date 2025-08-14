# Project Kessef

Skeleton for a personal financial planner and budget tracker application.

This project provides a minimal Python package for tracking income and expenses,
computing category totals, and calculating the current balance.  It is intended
as a starting point for further development into a full-featured application.

## Layout

- `finance_tracker/` – core package with budget and transaction models.
- `tests/` – unit tests executed with `pytest`.

## Development

Create a virtual environment, install dependencies, and run tests:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```
