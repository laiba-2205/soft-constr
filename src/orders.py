def calc(order):
    subtotal = 0
    for item in order["items"]:
        price = item["price"]
        quantity = item["qty"]
        if price > 0:
            if quantity > 0:
                subtotal = subtotal + price * quantity

    if order["member"] == True:
        if subtotal > 100:
            discount = subtotal * 0.2
        elif subtotal > 50:
            discount = subtotal * 0.1
        else:
            discount = 0
    else:
        discount = 0

    subtotal = subtotal - discount

    if order["country"] == "PK":
        shipping = 5
    elif order["country"] == "US":
        shipping = 15
    else:
        shipping = 25

    total = subtotal + shipping
    print("Total: " + str(total))
    return total