def count_cart(cart):
    total_quantity, total_amount = 0, 0
    if cart:
        for c in cart.value():
            total_quantity += c['quantity']
            total_amount += c['quantity']*c['price']
    return{
        'total_quantity': total_quantity,
        'total_price': total_amount
    }