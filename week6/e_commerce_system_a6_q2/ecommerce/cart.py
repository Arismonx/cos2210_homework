def add_item(cart_list, item_name, price):
    """
    Add item to cart list

    cart_list: cart
    item_name: item name
    price: price item

    Returns:
    cart_list:
    """
    dictionary = {"name": item_name, "price": price}
    cart_list.append(dictionary)

    return cart_list


def remove_item(cart_list, item_name):
    """
    Remove item from cart list

    cart_list: cart
    item_name: item name

    Returns:
    cart_list:
    """
    for i in range(len(cart_list)):
        if cart_list[i]["name"] == item_name:
            cart_list.pop(i)
            break

    return cart_list


def calculate_total(cart_list):
    """
    Calculate total price

    cart_list: cart

    Returns:
    total: total price
    """
    total = 0.0
    for i in range(len(cart_list)):
        total += cart_list[i]["price"]

    return total


def apply_discount(total_price, percent):
    """
    Calculate discount

    total_price: total price
    percent: percent

    Returns Net price
    """
    return (total_price * (100 - percent)) / 100
