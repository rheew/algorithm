import re
N = int(input())
ans = 0
num = 666
while N != ans:
    if re.search('666', str(num)):
        ans += 1
    num += 1

print(num-1)