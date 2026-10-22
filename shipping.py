# shipping.py
from billing import final_price

def shipping_cost(weight):
    return weight * 5

def order_total(amount, weight):
    return final_price(amount) + shipping_cost(weight)
