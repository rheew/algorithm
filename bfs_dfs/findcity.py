import sys
from collections import deque
input = sys.stdin.readline

N, M, D, S = map(int, input().rstrip().split())

li = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().rstrip().split())
    li[a].append(b)

visit = [False for _ in range(N+1)]
def BFS(start):
    d = deque()
    d.append((start, 0))
    ans = []
    while(len(d)):
        cur, dis = d.popleft()
        if dis == D:
            ans.append(cur)
            continue
        for i in li[cur]:
            if visit[i] : continue
            visit[i] = True
            d.append((i,dis+1))
    return ans

ans = BFS(S)
ans.sort()
for i in ans:
    print(i)

if not len(ans) : print(-1)