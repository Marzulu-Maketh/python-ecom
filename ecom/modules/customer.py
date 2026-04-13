from .user import User

class Customer(User):
    def __init__(self, name, phone_no, address, payment_method,ordererd_items=[],wishlist=[]):
        super().__init__(name, phone_no, address)
        self._payment_method = payment_method
        self._ordered_items = ordererd_items
        self._wishlist = wishlist

    def order_item(self, item_id, quantity, seller):
        item_to_be_sold = seller.get_catalogue[item_id]
        
        item_stock = item_to_be_sold["stock"]
        item_price = item_to_be_sold["price"]
        item_name = item_to_be_sold["name"]

        if quantity > item_stock:
            print(f'{item_name}\'s stock is lower than ordered quantity by {quantity-item_stock} units')
            return
        
        sub_total = item_price*quantity

        print(f'Making an order of {quantity} {item_name} for a total of {sub_total}')

        seller.sell_item(self, item_id, quantity, sub_total)

    
