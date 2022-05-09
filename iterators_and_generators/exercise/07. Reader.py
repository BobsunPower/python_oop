def read_next(*args):
    for el in args:
        for sub in el:
            yield str(sub)
