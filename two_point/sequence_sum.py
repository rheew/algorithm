import sys

input = sys.stdin.readline

N = int(input().rstrip())

num = []
visit = [False] * (N+1)

for i in range(2, N+1) :
    if visit[i] : continue
    num.append(i)
    for j in range(i ,N+1, i):
        visit[j] = True

ans = 0
pre = 0
total = 0
for i in range(0, len(num)) :
    total += num[i]
    while total > N and pre < len(num):
        total -= num[pre]
        pre += 1
    if total == N : ans += 1

print(ans)