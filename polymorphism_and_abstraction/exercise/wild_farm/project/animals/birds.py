# from polymorphism_and_abstraction.exercise.wild_farm.project.animals.animal import Bird
# from polymorphism_and_abstraction.exercise.wild_farm.project.food import Vegetable, Meat, Seed, Fruit
from project.animals.animal import Bird
from project.food import Vegetable, Meat, Seed, Fruit


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.foods = [Meat]
        self.gains = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.foods = [Vegetable, Meat, Seed, Fruit]
        self.gains = 0.35

    def make_sound(self):
        return "Cluck"
