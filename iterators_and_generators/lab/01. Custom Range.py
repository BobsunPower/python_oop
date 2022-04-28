class custom_range:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.value = self.start

    def __iter__(self):
        return self

    def __next__(self):
        temp_value = self.value
        if temp_value > self.end:
            raise StopIteration

        self.value += 1
        return temp_value
