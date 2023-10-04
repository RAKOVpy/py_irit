line = input()
a = ''
b = ''
c = ''
flag_num = 0
for i in line:
    if i == '.':
        flag_num += 1
        continue
    if flag_num == 0:
        a += i
    elif flag_num == 1:
        b += i
    else:
        c += i

print(c)
print(b)
print(a)
