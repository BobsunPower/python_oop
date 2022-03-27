class Person:
    def __init__(self, name: str, age: int):
        self._Person__name, self._Person__age = name, age

    def get_name(self):
        return self._Person__name

    def get_age(self):
        return self._Person__age
