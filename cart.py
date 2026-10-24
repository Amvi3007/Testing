from rates import get_rate


def total(amount):
    return amount - get_rate("IN")
