# from polymorphism_and_abstraction.exercise.animals.project.cat import Cat
from project.cat import Cat


class Kitten(Cat):
    gender = "Female"

    def __init__(self, name, age):
        super().__init__(name, age, Kitten.gender)
        self.sound = "Meow"
