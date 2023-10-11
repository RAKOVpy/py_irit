n = int(input())
m = [[j for j in range(1, n + 1)] for _ in range(n)]
ans = [[m[j][i] for j in range(n)] for i in range(n)]
print_ans = lambda x: print(*x, sep=', ')
[print_ans(i) for i in m]
print()
[print_ans(i) for i in ans]
