import sys
import re

c = re.compile('\.\.+')
input = sys.stdin.readline

N = int(input().rstrip())

li = [input().rstrip() for _ in range(N)]

def find(m) :
    sum = 0
    for i in m:
        sum += len(c.findall(i))
    print(sum, end=' ')

find(li)
sum = 0
for i in list(zip(*li)):
    sum += len(c.findall(''.join(i)))

print(sum)