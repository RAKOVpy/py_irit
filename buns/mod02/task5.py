line = input()
a = ''
n = ''
flag_num = False
for i in line:
    if i == ',':
        flag_num = True
        continue
    if not flag_num:
        a += i
    else:
        n += i

n = int(n)

n_index = ord(a) - 97
print(chr((n_index + n) % 26 + 97))
