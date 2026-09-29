def get_items_subtotal(items):
    subtotal = 0
    for item in items:
        price = item["price"]
        quantity = item["qty"]
        if price > 0:
            if quantity > 0:
                subtotal = subtotal + price * quantity
    return subtotal

def get_member_discount(member, subtotal):
    if member == True:
        if subtotal > 100:
            discount = subtotal * 0.2
        elif subtotal > 50:
            discount = subtotal * 0.1
        else:
            discount = 0
    else:
        discount = 0
    return discount

def get_shipping_cost(country):
    if country == "PK":
        shipping = 5
    elif country == "US":
        shipping = 15
    else:
        shipping = 25
    return shipping

def calc(order):
    subtotal = get_items_subtotal(order["items"])
    discount = get_member_discount(order["member"], subtotal)
    
    subtotal = subtotal - discount
    
    shipping = get_shipping_cost(order["country"])
    
    total = subtotal + shipping
    print("Total: " + str(total))
    return total
