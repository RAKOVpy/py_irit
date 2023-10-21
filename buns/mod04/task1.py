m = [int(i) for i in input().split()]
unique = set(m)
if len(unique) == len(m):
    print('Все числа разные')
elif len(unique) == 1:
    print('Все числа равны')
else:
    print('Есть равные и неравные числа')
