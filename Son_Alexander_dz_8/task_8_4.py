def val_checker(callback):

    def _val_checker(func):

        def wrapper(*args):
            numbers = list(map(callback, args))
            for i, arg in zip(numbers, args):
                if i is False:
                    msg = f'wrong val {arg}'
                    raise ValueError(msg)

            for arg in args:
                number = arg
                return func(arg)

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0, )
# @val_checker()
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
# b = calc_cube(-1)

print(a)
# print(b)
