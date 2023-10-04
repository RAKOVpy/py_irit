line = input()
a = ''
b = ''
c = ''
flag_num = 0
for i in line:
    if i == ' ':
        flag_num += 1
        continue
    if flag_num == 0:
        a += i
    elif flag_num == 1:
        b += i
    else:
        c += i

a = int(a)
b = int(b)
c = int(c)

ans = 0
if a >= b and a >= c:
    if b > c:
        ans = b
    else:
        ans = c
elif b >= a and b >= c:
    if a > c:
        ans = a
    else:
        ans = c
else:
    if a > b:
        ans = a
    else:
        ans = b

print(ans)
