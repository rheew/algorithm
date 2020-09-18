import sys
from collections import deque

input = sys.stdin.readline
INF = 10001
N = int(input().rstrip())
parents = list(map(int, input().rstrip().split()))
target = int(input().rstrip())
node = [[] for _ in range(N)]
parents[target] = -2

for i in range(0, N) :
    if parents[i] < 0 : continue
    node[parents[i]].append(i)


ans = 0
def BFS(start) :
    global ans
    d = deque()
    d.append(start)
    while d :
        now = d.popleft()

        if not node[now] : ans += 1

        for i in node[now] :
            d.append(i)

for i in range(len(parents)) :
    if parents[i] == -1 :
        BFS(i)

print(ans)