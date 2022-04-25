# from polymorphism_and_abstraction.exercise.wild_farm.project.animals.animal import Mammal
# from polymorphism_and_abstraction.exercise.wild_farm.project.food import Vegetable, Fruit, Meat
from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.foods = [Vegetable, Fruit]
        self.gains = 0.1

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.foods = [Meat]
        self.gains = 0.4

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.foods = [Vegetable, Meat]
        self.gains = 0.3

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.foods = [Meat]
        self.gains = 1

    def make_sound(self):
        return "ROAR!!!"
