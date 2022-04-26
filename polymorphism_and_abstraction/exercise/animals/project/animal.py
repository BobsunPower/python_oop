from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name, self.age, self.gender, self.sound = name, age, gender, None

    @abstractmethod
    def __repr__(self):
        pass

    def make_sound(self):
        return self.sound
