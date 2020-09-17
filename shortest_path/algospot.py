import sys
import heapq

input = sys.stdin.readline
INF = int(1e10)
N, M = map(int, input().rstrip().split())


board = [[int(i) for i in input().rstrip()] for _ in range(M)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
dis = [[INF] * N for _ in range(M)]

def BFS(x, y) :
    h = []
    heapq.heappush(h, (x, y, 0))
    dis[x][y] = 0
    while h :
        x, y, cost = heapq.heappop(h)

        if cost > dis[x][y] : continue
        if x == N and y == M : continue

        for i in range(4) :
            nx, ny = dx[i] + x, dy[i] + y

            if nx >= M or nx < 0 or ny < 0 or ny >= N : continue
            sumcost = dis[x][y] + board[nx][ny]
            if dis[nx][ny] > sumcost :
                dis[nx][ny] = sumcost
                heapq.heappush(h, (nx, ny, sumcost))

BFS(0,0)
print(dis[M-1][N-1])