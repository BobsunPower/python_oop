class Account:
    def __init__(self, id, name, balance=0):
        self.id, self.name, self.balance = id, name, balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount > self.balance:
            return "Amount exceeded balance"
        self.balance -= amount
        return self.balance

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"
