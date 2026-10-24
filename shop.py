def calculate_tax(subtotal, rate):
    return subtotal * rate


def final_price(subtotal):
    tax = calculate_tax(subtotal, 0.18)
    return subtotal + tax
