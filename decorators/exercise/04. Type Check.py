def type_check(type_to_check):
    def decorator(function):
        def wrapper(*args):
            if isinstance(*args, type_to_check):
                return function(*args)
            return "Bad Type"

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


@type_check(str)
def first_letter(word):
    return word[0]
