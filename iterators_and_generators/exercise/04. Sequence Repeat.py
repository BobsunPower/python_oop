class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence, self.number, self.index, self.counter = sequence, number, 0, 0
        self.elements_in_seq = len(self.sequence)

    def __iter__(self):
        return self

    def __next__(self):
        work_number = self.index
        if self.counter == self.number:
            raise StopIteration
        self.counter += 1
        self.index += 1
        if self.index == self.elements_in_seq:
            self.index = 0
        return self.sequence[work_number]
