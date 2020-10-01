import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
a, b = map(int, input().rstrip().split())

M = int(input().rstrip())
node = [[] for _ in range(N + 1)]

for _ in range(M) :
    x, y = map(int, input().rstrip().split())
    node[x].append(y)
    node[y].append(x)

def BFS() :
    q = deque()
    q.append((a,0))
    visit = [False] * (N + 1)

    while q :
        now, cost = q.popleft()
        if now == b : return cost
        for i in node[now] :
            if visit[i] : continue
            visit[i] = True
            q.append((i, cost + 1))

    return -1

print(BFS())