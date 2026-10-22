def calculate_tax(amount: float, rate: float = 0.18) -> float:
    if amount < 0:
        raise ValueError("amount cannot be negative")
    return round(amount * rate, 2)


