from .user import User

class Customer(User):
    def __init__(self, name, phone_no, address, payment_method,ordererd_items=[],wishlist=[]):
        super().__init__(name, phone_no, address)
        self._payment_method = payment_method
        self._ordered_items = ordererd_items
        self._wishlist = wishlist

    #Getters
    @property
    def get_ordered_items(self):
        return self._ordered_items

    @property
    def get_wishlist(self):
        return self._wishlist
    
    #Setters
    def add_wishlist(self, item):
        self._wishlist.append(item)

    def add_to_ordered_list(self, item):
        self._ordered_items.append(item)

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

    def wishlist_item(self, item_id, quantity, seller):
        wishlisted_item = seller.get_catalogue[item_id]
        
        item_stock = wishlisted_item["stock"]
        item_price = wishlisted_item["price"]
        item_name = wishlisted_item["name"]

        if quantity > item_stock:
            print(f'{item_name}\'s stock is lower than ordered quantity by {quantity-item_stock} units')
            return

        sub_total = item_price*quantity

        item = { "item_name": item_name, "item_id":item_id, "quantity":quantity, "price":item_price, "sub_total":sub_total, "seller_uuid":seller.get_id }

        self.add_wishlist(item)

        print(f'{quantity} of {item_name} for a total of {sub_total} has been wishlisted')

    def eliminate_wishlist(self, item):
        wishlist = self.get_wishlist
        for i in range(len(wishlist)):
            if wishlist[i] == item:
                if wishlist[i]["quantity"] - item["quantity"] <= 0:
                    wishlist.pop(i)
                else:
                    wishlist[i]["quantity"] -= item["quantity"]
