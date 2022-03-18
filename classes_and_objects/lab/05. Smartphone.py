class Smartphone:
    def __init__(self, memory):
        self.memory, self.apps, self.is_on = memory, [], False

    def power(self):
        self.is_on = False if self.is_on else True

    def install(self, app, memory):
        if self.memory < memory:
            return f"Not enough memory to install {app}"
        if not self.is_on:
            return f"Turn on your phone to install {app}"
        self.memory -= memory
        self.apps.append(app)
        return f"Installing {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
