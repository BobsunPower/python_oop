class dictionary_iter:
    def __init__(self, input_dict: dict):
        self.input_dict, self.start_point = input_dict, 0
        self.pairs = list(self.input_dict.items())
        self.end_point = len(self.pairs) - 1

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.start_point
        if self.start_point > self.end_point:
            raise StopIteration

        self.start_point += 1
        return self.pairs[temp]
