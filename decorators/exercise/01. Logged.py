def logged(function):
    def wrapper(*args):
        return f"you called {function.__name__}{args}\nit returned {function(*args)}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


@logged
def sum_func(a, b):
    return a + b
