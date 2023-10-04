def int_to_y(x, y):
    if x == 0 or y == 0:
        return '0'
    t = x
    ans = ''
    while t > 0:
        temp = str(t % y)
        if int(temp) < 10:
            ans += str(t % y)
        else:
            ans += chr(65 + int(temp) - 10)
        t //= y
    return ans[::-1]


n = input()
if '.' not in n or float(n) < 0:
    n = int(n)
    print(int_to_y(n, 2), int_to_y(n, 8), int_to_y(n, 16), sep=', ')
else:
    print('Неверный ввод')
