def type_logger(func):
    # print(type())

    def wrapper(*args):
        for i in args:
            return f'{i}: {type(i)}'

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(6)

print(a)
