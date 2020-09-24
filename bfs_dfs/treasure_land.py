import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

board = [input().rstrip() for i in range(N)]
ans = 1
dx, dy = [1,-1,0,0], [0,0,-1,1]

def BFS(x, y) :
    d = deque()
    d.append((x,y,0))
    visit = [[False] * M for _ in range(N)]
    ans = 0
    visit[x][y] = True
    while d :
        x, y, cost = d.popleft()
        ans = max(ans, cost)
        for i in range(4) :
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M :
                if visit[nx][ny] or board[nx][ny] != 'L' : continue
                visit[nx][ny] = True
                d.append((nx, ny, cost+1))

    return ans

for i in range(N) :
    for j in range(M) :
        if board[i][j] == 'L' :
            ans = max(ans, BFS(i,j))
print(ans)