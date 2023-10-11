s = input()
ans = [i for i in s if i not in {'-', ')', '(', ' '}]
print(*ans, sep='')
