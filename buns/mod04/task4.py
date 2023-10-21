s = input()
ans = ''
middle = ''
for i in set(s):
    t = s.count(i)
    if t % 2 != 0 and not middle:
        middle = i * t
        continue
    elif t % 2 != 0:
        raise Exception('Нельзя составить палиндром')
    ans += i * (t // 2)
ans = ans + middle + ans[::-1]
print(ans)
