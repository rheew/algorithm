import sys
from collections import Counter

input = sys.stdin.readline

N = int(input().rstrip())
first = Counter()
ans = 0

for j in range(N):
    s = input().rstrip()
    cs = Counter(s)
    if len(first) == 0 :
        first = cs
        continue

    result1 = first - cs
    result2 = cs - first

    result1 = sum(result1.values())
    result2 = sum(result2.values())

    if max(result1, result2) > 1: continue
    ans += 1

print(ans)