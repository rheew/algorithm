from collections import deque
import sys
input = sys.stdin.readline

s = input().rstrip()
boom = input().rstrip()
d = deque()
lenboom = len(boom)
for i in s:
    d.append(i)
    if len(d) >= lenboom:
        flag = False
        for j in range(1,lenboom+1):
            if boom[-j] != d[-j]:
                flag = True
                break

        if flag : continue

        for _ in range(lenboom):
            d.pop()

print(''.join(d) if d else 'FRULA')