def f(n1, n2):
    if n1 == 0:
        return n2
    return f(n2 % n1, n1)
