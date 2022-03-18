class Cup:
    def __init__(self, size, quantity):
        self.size, self.quantity = size, quantity

    def fill(self, milliliters):
        if self.quantity + milliliters <= self.size:
            self.quantity += milliliters

    def status(self):
        return self.size - self.quantity
