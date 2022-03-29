class Account:
    def __init__(self, id: int, balance: int, pin: int):
        self.__id, self.balance, self.__pin = id, balance, pin

    def get_id(self, pin):
        if pin == self.__pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"
