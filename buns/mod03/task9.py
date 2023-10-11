N = int(open('input9.txt').readline())
len_ans, i = 0, 0
ans = [0, 0]
while True:
    for _ in range((i + 2) // 2):
        if len_ans == N:
            open('output9.txt', mode='w').write(f'{ans[0]} {ans[1]}')
            exit()
        ans = [ans[0] - (i % 4 == 0) + (i % 4 == 2), ans[1] - (i % 4 == 1) + (i % 4 == 3)]
        len_ans += 1
    i += 1
