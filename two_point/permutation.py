import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

temperature = list(map(int, input().rstrip().split()))
pre = 0
total = 0

for i in range(M):
    total += temperature[i]
ans = total

for i in range(M, N):

    total -= temperature[pre]
    total += temperature[i]
    pre += 1
    ans = max(ans, total)

print(ans)