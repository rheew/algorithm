import sys
import heapq

input = sys.stdin.readline
INF = int(1e10)

N, M, tar = map(int, input().rstrip().split())

node = [[] for _ in range(N + 1)]

for i in range(M) :
    a, b, cost = map(int,input().rstrip().split())

    node[a].append((b,cost))


def dij(start, end) :
    h = []
    heapq.heappush(h, (0, start))
    dis = [INF] * (N + 1)
    dis[start] = 0

    while h :
        cost, now = heapq.heappop(h)

        if cost > dis[now] : continue

        for ind, value in node[now] :
            sum_dis = value + cost
            if sum_dis >= dis[ind] : continue

            dis[ind] = sum_dis
            heapq.heappush(h, (sum_dis, ind))

    return dis[end]

ans = 0
for i in range(1,N + 1) :
    start_cost = dij(i, tar)
    return_cost = dij(tar, i)
    ans = max(ans, start_cost + return_cost)

print(ans)