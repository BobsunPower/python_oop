class Flower:
    def __init__(self, name, water_requirements):
        self.name, self.water_requirements, self.is_happy = name, water_requirements, False

    def water(self, quantity):
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self):
        return f'{self.name} is happy' if self.is_happy else f'{self.name} is not happy'