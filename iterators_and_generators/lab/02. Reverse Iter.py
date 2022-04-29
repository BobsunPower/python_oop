class reverse_iter:
    def __init__(self, iterable):
        self.iterable, self.starting_point, self.end_point = iterable, len(iterable) - 1, 0
        self.work_value = self.starting_point

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.work_value
        if self.work_value < self.end_point:
            raise StopIteration
        self.work_value -= 1
        return self.iterable[temp]
