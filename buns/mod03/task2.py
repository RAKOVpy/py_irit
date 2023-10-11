n = int(input())
ans = map(lambda x: x[2:], [bin(n), oct(n), hex(n).upper()])
print(*ans)
