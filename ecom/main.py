from modules.seller import Seller
from modules.customer import Customer
from modules.utils import *

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