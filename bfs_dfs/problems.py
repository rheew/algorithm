import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

visit = [False] * N
nodes = [[] for _ in range(N + 1)]
degree = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    degree[b] += 1
    nodes[a].append(b)

q = []

for i in range(1, N + 1):
    if degree[i] == 0 :
        heapq.heappush(q, i)

while q :
    now = heapq.heappop(q)

    print(now, end=' ')

    for i in nodes[now]:
        degree[i] -= 1
        if degree[i] == 0 :
            heapq.heappush(q, i)
