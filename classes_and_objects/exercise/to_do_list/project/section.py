# from classes_and_objects.exercise.to_do_list.project.task import Task
from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name, self.tasks = name, []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for t in self.tasks:
            if t.name == task_name:
                t.completed = True
                return f"Completed task {t.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        return f"Cleared {len([self.tasks.remove(task) for task in [t for t in self.tasks if t.completed]])} tasks."

    def view_section(self):
        nl = "\n"
        return f"Section {self.name}:\n{nl.join([t.details() for t in self.tasks])}"
