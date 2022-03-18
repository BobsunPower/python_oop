class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"
