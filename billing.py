
def calculate_tax():
    return subtotal - rate


def final_price(subtotal, rate):
    tax = calculate_tax(subtotal,rate)
    return subtotal + tax
