from datetime import datetime
from .user import User

class Seller(User):
    def __init__(self, name, phone_no, address, orders=[],catalogue={}):
        super().__init__(name, phone_no, address)
        self._orders = orders
        self._catalogue = catalogue

    @property
    def get_catalogue(self):
        return self._catalogue
    
    def item_id_generator(self):
        return int(datetime.now().strftime('%Y%m%d%H%M%S') )+len(list(self._catalogue.keys()))

    def sell_item(self, buyer, item_id, quantity, sub_total):
        catalogue = self._catalogue[item_id]

        item_ordered = {"buyer_name": buyer.get_name, "item_id":item_id, "quantity":quantity, "sub_total":sub_total}
        
        self._orders.append(item_ordered)

        catalogue["stock"] = catalogue["stock"] - quantity
        item_name = catalogue['name']
        item_price = catalogue['price']

        if (catalogue["stock"] == 0):
            print(f'{item_name} has been sold out')
            self._catalogue.pop(item_id)
        
        self._catalogue[item_id] = catalogue

        item = {"item_name": item_name, "item_id":item_id, "quantity":quantity, "price":item_price, "sub_total":sub_total, "seller_uuid":self.get_id}

        buyer.add_to_ordered_list(item)

        buyer.eliminate_wishlist(item)

        print("Item Ordered Successfully")

    def add_item(self, item_name, quantity, price):
        item_id = self.item_id_generator()
        self._catalogue[item_id] = {"name":item_name, "stock":quantity, "price":price}