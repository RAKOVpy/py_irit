line = input() + ' '
ans = ''
temp = ''

for i in line:
    if i == ' ' and temp != ' ':
        ans += temp

    temp = i

print(ans)
