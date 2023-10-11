n = int(input())
ans = map(lambda x: x[2:], [bin(n), oct(n), hex(n).upper()])
print(*ans) if n >= 0 else print('Неверный ввод')
