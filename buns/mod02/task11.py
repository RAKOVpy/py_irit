line = input()
good_line = ''
for i in line:
    if i == '-':
        continue
    good_line += i

m = [i for i in good_line if i != ' ']
ans_check = len(m) != len(set(m))

box = ''
flag = False
for i in good_line:
    if i == ' ':
        continue

    if i in box:
        flag = True
        break

    box += i

print(flag)
