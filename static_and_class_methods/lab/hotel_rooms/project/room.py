class Room:
    def __init__(self, number, capacity):
        self.number, self.capacity, self.guests, self.is_taken = number, capacity, 0, False

    def take_room(self, people):
        if not self.is_taken and people <= self.capacity:
            self.guests += people
            self.is_taken = True
            return None
        return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guests = 0
        else:
            return f"Room number {self.number} is not taken"
