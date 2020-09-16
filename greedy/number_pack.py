import sys
import math

input = sys.stdin.readline
INF = 10001
N = int(input().rstrip())

numbers = [int(input().rstrip()) for _ in range(N)]

numbers.sort(reverse=True)
pre = INF
result = []

positive = []
negative = []
zero = 0

for i in numbers :
    if i == 0 : zero += 1
    elif i > 1 : positive.append(i)
    elif i == 1 : result.append(1)
    else : negative.append(i)

positive.sort(reverse=True)
negative.sort()

for i in range(len(positive)) :
    if pre == INF :
        pre = positive[i]
        continue

    result.append(pre * positive[i])
    pre = INF

if pre != INF : result.append(pre)
pre = INF

for i in range(len(negative)):
    if pre == INF:
        pre = negative[i]
        continue

    result.append(pre * negative[i])
    pre = INF

if pre != INF:
    if zero == 0 : result.append(pre)

print(sum(result))