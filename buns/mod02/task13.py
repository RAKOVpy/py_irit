line = input()
cnt = 1
s = 0

for i in line:
    if cnt % 2 == 0:
        s += 3 * int(i)
    else:
        s += int(i)
    cnt += 1
    cnt %= 2

if s % 10 == 0:
    print('yes')
else:
    print('no')
