import uuid

class User:
    def __init__(self, name, phone_no, address):
        self._name = name
        self._phone_no = phone_no
        self._address = address
        self._uuid = uuid.uuid4()

    #Getters
    @property
    def get_name(self):
        return self._name
    
    @property
    def get_phone_number(self):
        return self._phone_no

    @property
    def get_address(self):
        return self._address
    
    @property
    def get_id(self):
        return self._uuid

    #Setters
    def set_name(self, name):
        self._name = name

    def set_phone_number(self, phone_no):
        self._phone_no = phone_no
    
    def set_address(self, address):
        self._address = address