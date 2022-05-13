from itertools import permutations


def possible_permutations(values):
    for el in permutations(values):
        yield list(el)
