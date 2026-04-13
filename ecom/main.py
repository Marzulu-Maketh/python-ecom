from modules.seller import Seller
from modules.customer import Customer

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

#For Now
def add_dummy_items(seller):
    seller.add_item("Dummy", 100, 30)

def user_interation(customer, seller):
    print("Please Select the following options")
    print("A) Buy\nB) Exit")
    user_input = input(":\t").lower()

    if user_input == 'a':
        display_items(customer, seller)
    elif user_input == 'b':
        print("Thanks for visiting")
    else:
        print('Invalid Input')

    if user_input != 'b':
        user_interation(customer, seller)


def main():
    print("Welcome to the store")

    name = input("Please enter your name: ")
    phone_no = take_in_numeric_input("Please enter your Phone Number: ")
    address = input("Please enter your Address: ")
    payment_method = input("Please enter your payment method: ")

    customer = Customer(name, phone_no, address, payment_method)
    seller = Seller("Koch", 911, "EL 235 Carbide")

    for i in range(10):
        add_dummy_items(seller)

    user_interation(customer, seller)


if __name__ == "__main__":
    main()