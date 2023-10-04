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

a = int(a)
b = int(b)

print(a % b)
