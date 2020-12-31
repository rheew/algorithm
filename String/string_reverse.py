import sys
from collections import deque

input = sys.stdin.readline

s = input().rstrip()

def reverse(s):
    result = ''

    for i in s:
        result = i + result

    return result

q = deque()
result = ''
reversestr = ''

for j in s:
    if j == '<':
        q.append(j)
        result += reverse(reversestr)
        reversestr = ''

    elif j == '>':
        result += j
        q.popleft()
        continue

    if len(q) > 0:
        result += j
        continue

    if j == ' ':
        result += reverse(reversestr) + ' '
        reversestr = ''
        continue
    reversestr += j

print(result + reverse(reversestr))