import functools


def multiply(times):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * times

        return wrapper

    return decorator


@multiply(5)
def add_ten(number):
    return number + 10
