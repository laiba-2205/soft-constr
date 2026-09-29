def get_items_subtotal(items):
    subtotal = 0
    for item in items:
        price = item["price"]
        quantity = item["qty"]
        if price <= 0 or quantity <= 0:
            continue
        subtotal = subtotal + price * quantity
    return subtotal

def get_member_discount(member, subtotal):
    if not member:
        return 0
    if subtotal > 100:
        return subtotal * 0.2
    if subtotal > 50:
        return subtotal * 0.1
    return 0

def get_shipping_cost(country):
    if country == "PK":
        return 5
    if country == "US":
        return 15
    return 25

def calc(order):
    subtotal = get_items_subtotal(order["items"])
    
    discount = get_member_discount(order["member"], subtotal)
    
    subtotal = subtotal - discount
    
    shipping = get_shipping_cost(order["country"])
    
    total = subtotal + shipping
    print("Total: " + str(total))
    return total
