# TODO
class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []
        self.type_of_animals = {"Lion": [], "Tiger": [], "Cheetah": [], "total": 0}
        self.type_of_workers = {"Caretaker": [], "Keeper": [], "Vet": [], "total": 0}

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity:
            if price <= self.__budget:
                self.animals.append(animal)
                self.__budget -= price
                self.type_of_animals[type(animal).__name__].append(animal)
                self.type_of_animals["total"] += 1

                return f"{animal.name} the {type(animal).__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            self.type_of_workers[type(worker).__name__].append(worker)
            self.type_of_workers["total"] += 1
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                self.type_of_workers[type(worker).__name__].remove(worker)
                self.type_of_workers["total"] -= 1
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        money_needed = sum([worker.salary for worker in self.workers])
        if money_needed <= self.__budget:
            self.__budget -= money_needed
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_needed = sum([animal.money_for_care for animal in self.animals])
        if money_needed <= self.__budget:
            self.__budget -= money_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = [f'You have {self.type_of_animals["total"]} animals',
                  f'----- {len(self.type_of_animals["Lion"])} Lions:']
        for lion in self.type_of_animals["Lion"]:
            result.append(f"{lion}")
        result.append(f'----- {len(self.type_of_animals["Tiger"])} Tigers:')
        for tiger in self.type_of_animals["Tiger"]:
            result.append(f"{tiger}")
        result.append(f'----- {len(self.type_of_animals["Cheetah"])} Cheetahs:')
        for cheetah in self.type_of_animals["Cheetah"]:
            result.append(f"{cheetah}")
        return "\n".join(result)

    def workers_status(self):
        result = [f'You have {self.type_of_workers["total"]} workers',
                  f'----- {len(self.type_of_workers["Keeper"])} Keepers:']
        for keeper in self.type_of_workers["Keeper"]:
            result.append(f"{keeper}")
        result.append(f'----- {len(self.type_of_workers["Caretaker"])} Caretakers:')
        for caretaker in self.type_of_workers["Caretaker"]:
            result.append(f"{caretaker}")
        result.append(f'----- {len(self.type_of_workers["Vet"])} Vets:')
        for vet in self.type_of_workers["Vet"]:
            result.append(f"{vet}")
        return "\n".join(result)
