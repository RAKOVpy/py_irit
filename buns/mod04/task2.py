def f(a, n):
    if n == 0:
        return 0
    if n == 1:
        return a
    if n % 2 == 0:
        return f(a * a, n // 2)
    return a * f(a, n - 1)
