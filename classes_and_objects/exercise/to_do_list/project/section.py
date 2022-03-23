from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name, self.tasks = name, []

    def add_task(self, task):
        if task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(task)
        return f"Task {task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        return f"Cleared {len([self.tasks.remove(task) for task in [task for task in self.tasks if task.completed]])} tasks."

    def view_section(self):
        nl = "\n"
        return f"Section {self.name}:\n{nl.join([el.details() for el in self.tasks])}"
