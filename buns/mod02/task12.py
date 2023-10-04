line = input()
box = '-)( '
ans = ''

for i in line:
    if i not in box:
        ans += i

print(ans)
