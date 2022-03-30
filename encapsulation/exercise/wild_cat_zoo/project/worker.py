class Worker:
    def __init__(self, name: str, age: int, salary: int):
        self.name, self.age, self.salary = name, age, salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
