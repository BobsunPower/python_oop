def even_parameters(function):
    def wrapper(*args):
        for el in args:
            if isinstance(el, str) or not el % 2 == 0:
                return "Please use only even numbers!"
        return function(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result
