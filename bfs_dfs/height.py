import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

up = [[] for _ in range(N + 1)]
down = [[] for _ in range(N + 1)]

for _ in range(M) :
    x, y = map(int, input().rstrip().split())

    up[x].append(y)
    down[y].append(x)

def BFS(node, start) :
    d = deque()
    d.append(start)
    visit = [False] * (N + 1)
    cnt = 0

    while d :
        now = d.popleft()

        for i in node[now] :
            if visit[i] : continue
            visit[i] = True
            cnt += 1
            d.append(i)

    return cnt

ans = 0

for i in range(1, N + 1) :
    temp = BFS(up, i)
    temp += BFS(down, i)

    if temp == N - 1 : ans += 1

print(ans)