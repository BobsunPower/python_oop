# from inheritance.lab.multiple_inheritance.project.person import Person
# from inheritance.lab.multiple_inheritance.project.employee import Employee
from project.person import Person
from project.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
