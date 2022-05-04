class take_skip:
    def __init__(self, step, count):
        self.step, self.count, self._counter, self.work_value = step, count, 0, 0

    def __iter__(self):
        return self

    def __next__(self):
        work_value = self.work_value
        if self._counter == self.count:
            raise StopIteration

        self.work_value += self.step
        self._counter += 1
        return work_value
