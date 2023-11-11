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


@memoize
def fibonacci(n):
    """doc"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(70))
