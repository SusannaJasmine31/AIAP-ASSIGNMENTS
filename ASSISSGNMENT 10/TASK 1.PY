
def discount(price, category):
    if category == "student" and price > 1000:
        return price * 0.90
    elif category == "student":
        return price * 0.95
    elif price > 2000:
        return price * 0.85
    else:
        return price
print(discount(1500, "student"))  # Output: 1350.0
