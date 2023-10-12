def get_ans(m: list) -> str:
    def check_horizont(x: list):
        for i in range(n):
            if len(set(x[i])) == 1 and x[i][0] != '_':
                return x[i][0]

    n = len(m[0])
    vertic = [[m[j][i] for j in range(n)] for i in range(n)]
    if check_horizont(m):
        return check_horizont(m)
    if check_horizont(vertic):
        return check_horizont(vertic)
    flag = [True, True]
    for i in range(1, n):
        if m[i][i] != m[0][0]:
            flag[0] = False
        if m[i][-i - 1] != m[0][-1]:
            flag[1] = False
    if flag[0] and m[0][0] != '_':
        return m[0][0]
    if flag[1] and m[0][-1] != '_':
        return m[0][-1]
    return 'Ничья'


game = [[i for i in input() if i != ' ']]
game += [[i for i in input() if i != ' '] for i in range(len(game[0]) - 1)]
print(get_ans(game))
