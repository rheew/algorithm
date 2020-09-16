import sys
import heapq

input = sys.stdin.readline
INF = int(1e10)

N = int(input().rstrip())
M = int(input().rstrip())
node = [[] for _ in range(N + 1)]
dis = [INF] * (N + 1)

for _ in range(M) :
    x, y, c = map(int, input().rstrip().split())

    node[x].append((y,c))


s, e = map(int, input().rstrip().split())

def dij(start) :
    h = []
    heapq.heappush(h, (start, 0))
    dis[start] = 0
    while h :
        now, c = heapq.heappop(h)

        if c > dis[now] : continue

        for i, cost in node[now] :
            sumcost = cost + c
            if sumcost < dis[i]:
                dis[i] = sumcost
                heapq.heappush(h, (i, sumcost))

dij(s)

print(dis[e])