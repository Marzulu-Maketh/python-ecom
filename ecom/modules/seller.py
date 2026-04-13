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

        item_ordered = {"Buyer Name": buyer.get_name, "Item ID":item_id, "Quantity":quantity, "Sub Total":sub_total}
        
        self._orders.append(item_ordered)

        catalogue["stock"] = catalogue["stock"] - quantity

        if (catalogue["stock"] == 0):
            print(f'{catalogue['name']} has been sold out')
            self._catalogue.pop(item_id)
        
        self._catalogue[item_id] = catalogue

        print("Item Ordered Successfully")

    def add_item(self, item_name, quantity, price):
        item_id = self.item_id_generator()
        self._catalogue[item_id] = {"name":item_name, "stock":quantity, "price":price}