"""Simple tax rate helpers."""


def calculate_tax(amount: float, rate: float = 0.18) -> float:
    """Return the tax on `amount` at the given `rate` (default 18%)."""
    if amount < 0:
        raise ValueError("amount cannot be negative")
    return round(amount * rate, 2)
