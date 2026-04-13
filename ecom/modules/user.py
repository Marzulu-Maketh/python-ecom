class User:
    def __init__(self, name, phone_no, address):
        self._name = name
        self._phone_no = phone_no
        self._address = address

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

    #Setters
    @property
    def set_name(self, name):
        self._name = name

    @property
    def set_phone_number(self, phone_no):
        self._phone_no = phone_no
    
    @property
    def set_address(self, address):
        self._address = address