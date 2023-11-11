import time


class Timer:
    def __init__(self, func):
        self.func = func
        self.start_time = 0
        self.stop_time = 0

    def __call__(self, *args, **kw):
        if self.start_time:
            return self.func(*args, **kw)

        self.start_time = time.time()
        ans = self.func(*args, **kw)
        self.stop_time = time.time()
        print(self.stop_time - self.start_time)

        return ans


def memoize(func):
    d = dict()
    d['name_func'] = func.__name__
    d['doc_func'] = func.__doc__
    print(d['name_func'])
    print(d['doc_func'])

    def wrapper(n):
        if n in d:
            return d[n]
        ans = func(n)
        d[n] = ans
        return ans

    return wrapper


def validate_args(func):
    def wrapper(*args, **kwargs):
        if len(args) + len(kwargs) < 1:
            return 'Not enough arguments'
        if len(args) + len(kwargs) > 1:
            return 'Too many arguments'

        if args:
            num = args[0]
        else:
            num = kwargs[[*kwargs][0]]

        if int(num) != num:
            return 'Wrong types'
        if num < 0:
            return 'Negative argument'

        return func(*args, **kwargs)

    return wrapper


# @validate_args
# @Timer
# def fibonacci(n):
#     """doc"""
#     if n < 2:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(30))


@validate_args
@Timer
@memoize
def fibonacci(n):
    """doc"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(30))
