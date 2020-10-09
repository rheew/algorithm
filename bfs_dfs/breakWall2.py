import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e8)
N, M, K = map(int, input().rstrip().split())

board = [[int(i) for i in input().rstrip()] for _ in range(N)]

dx, dy = [0,0,1,-1], [1,-1,0,0]

def BFS(x, y) :
    d = deque()
    d.append((x, y, K, 1))
    visit = [[[False] * M for _ in range(N)] for _ in range(K + 1)]
    ans = INF

    while d :
        x, y, k, di = d.popleft()

        if x == N - 1 and y == M - 1:
            ans = min(ans, di)

        for i in range(4) :
            nx, ny = dx[i] + x, dy[i] + y
            if nx >= N or nx < 0 or ny >= M or ny < 0 : continue
            if visit[k][nx][ny]: continue

            if board[nx][ny] == 1 :
                if k == 0 : continue
                visit[k - 1][nx][ny] = True
                d.append((nx, ny, k - 1, di + 1))

            else :
                visit[k][nx][ny] = True
                d.append((nx, ny, k, di + 1))

    return ans

ans = BFS(0, 0)
if ans == INF : print(-1)
else : print(ans)

