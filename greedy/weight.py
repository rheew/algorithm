import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())

numbers = list(map(int, input().rstrip().split()))

numbers.sort()
totalsum = 0
ans = 0
for number in numbers :
    if number > totalsum + 1 :
        break
    totalsum += number

print(totalsum + 1)