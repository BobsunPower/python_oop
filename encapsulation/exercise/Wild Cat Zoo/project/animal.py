class Animal:
    def __init__(self, name: str, gender: str, age: int, money_for_care: int):
        self.name, self.gender, self.age, self.money_for_care = name, gender, age, money_for_care

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
