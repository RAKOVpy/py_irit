line = input()
cnt_0 = 0
cnt = 0
for i in line:
    cnt_0 += i == '0'
    cnt += 1

if cnt_0 == cnt - cnt_0:
    print('yes')
else:
    print('no')
