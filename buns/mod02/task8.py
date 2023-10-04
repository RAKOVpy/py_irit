line = input()
a = ''
b = ''
flag_num = False
for i in line:
    if i == ',':
        flag_num = True
        continue
    if not flag_num:
        a += i
    else:
        b += i

cnt = 0
for i in a:
    if i != b:
        break
    cnt += 1

print(cnt)
