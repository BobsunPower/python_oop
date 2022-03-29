class Person:
    def __init__(self, name: str, age: int):
        self.__name, self.__age = name, age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
