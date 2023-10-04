line = input()
gl = 'аеёиоуыэюя'

cnt_gl = 0
cnt_ngl = 0

for i in line:
    if i in gl:
        cnt_gl += 1
    elif i != ' ':
        cnt_ngl += 1

print(cnt_gl, cnt_ngl)
