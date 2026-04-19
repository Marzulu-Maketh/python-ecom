#This function is for handling numeric values with a try except error handling to prevent misinput
def take_in_numeric_input(string=":\t"):
    try:
        user_input = int(input(string))
    except:
        print("Invalid Input, must be numeric")
        return take_in_numeric_input()

    return user_input

def request_quantity():
    print("Enter the quantity of items you want to buy")
    return take_in_numeric_input()

#Displaying items from seller's catalogue
def display_items(customer, seller):
    catalogue = seller.get_catalogue


    i = 1
    for item_id in catalogue:
        item = catalogue[item_id]
        print(f'{i}) Name: {item["name"]} | Price: {item["price"]} | Stock: {item["stock"]}')
        i += 1

    print("Choose the following options")
    user_input = take_in_numeric_input() - 1

    if user_input <= len(list(catalogue.keys())) and user_input >= 0:
        quantity = request_quantity()
        item_id = list(catalogue.keys())[user_input]
        customer.order_item(item_id, quantity, seller)
    else:
        print("Invalid Input")
        return display_items(customer, seller)

#Displaying Wishlist from Customer's wishlist 
def display_wishlist(customer, seller):
    catalogue = seller.get_catalogue


    i = 1
    for item_id in catalogue:
        item = catalogue[item_id]
        print(f'{i}) Name: {item["name"]} | Price: {item["price"]} | Stock: {item["stock"]}')
        i += 1

    print("Choose the following options")
    user_input = take_in_numeric_input() - 1

    if user_input <= len(list(catalogue.keys())) and user_input >= 0:
        quantity = request_quantity()
        item_id = list(catalogue.keys())[user_input]
        customer.wishlist_item(item_id, quantity, seller)
    else:
        print("Invalid Input")
        return display_wishlist(customer, seller)

def display_wishlisted_items(customer):
    catalogue = customer.get_wishlist

    if len(catalogue) == 0:
        print("No ordered items")
        return

    i = 1
    for item in catalogue:
        print(f'{i}) Name: {item["item_name"]} | Price: {item["price"]} | Quantity: {item["quantity"]} | Sub Total: {item["sub_total"]}')
        i += 1

def display_ordered_items(customer):
    catalogue = customer.get_ordered_items

    if len(catalogue) == 0:
        print("No wishlisted items")
        return

    i = 1
    for item in catalogue:
        print(f'{i}) Name: {item["item_name"]} | Price: {item["price"]} | Quantity: {item["quantity"]} | Sub Total: {item["sub_total"]}')
        i += 1

#For Now
def add_dummy_items(seller):
    seller.add_item("Dummy", 100, 30)

def user_interation(customer, seller):
    print("Please Select the following options")
    print("A) Buy\nB) Wishlist Items\nC) Display wishlist\nD) Display Ordered Items\nE) Exit")
    user_input = input(":\t").lower()

    if user_input == 'a':
        display_items(customer, seller)
    elif user_input == 'b':
        display_wishlist(customer, seller)
    elif user_input == 'c':
        display_wishlisted_items(customer)
    elif user_input == 'd':
        display_ordered_items(customer)
    elif user_input == 'e':
        print("Thanks for visiting")
    else:
        print('Invalid Input')

    if user_input != 'e':
        user_interation(customer, seller)
