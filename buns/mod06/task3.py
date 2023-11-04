def armstrong_numbers():
    x = 1
    while True:
        x_str = str(x)
        n = len(x_str)
        check = sum([int(i) ** n for i in x_str])
        if not (check == x and (x > 9 or x == 1)):
            x += 1
            continue
        x += 1
        yield x - 1


iterat = armstrong_numbers()


def get_armstrong_numbers():
    return next(iterat)


for i in range(8):
    print(get_armstrong_numbers(), end=' ')
