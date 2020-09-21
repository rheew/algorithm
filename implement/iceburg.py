import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

board = [list(map(int, input().rstrip().split())) for _ in range(N)]
store = [[0] * M for _ in range(N)]

dx, dy = [0,0,1,-1], [1,-1,0,0]

def visit(x, y):

    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]

        if board[nx][ny] == 0 :
            store[x][y] += 1

def melt():
    for i in range(N):
        for j in range(M):
            board[i][j] -= store[i][j]
            if board[i][j] < 0 : board[i][j] = 0
            store[i][j] = 0

def BFS(x,y, visit):
    q = deque()
    q.append((x,y))
    visit[x][y] = True

    while q :
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if board[nx][ny] == 0 or visit[nx][ny] : continue
            visit[nx][ny] = True
            q.append((nx,ny))

def check():
    visit = [[False] * M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and not visit[i][j]:
                BFS(i,j, visit)
                cnt += 1

    return cnt

ans = 0
while True:
    ans += 1
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 :
                visit(i, j)

    melt()
    c = check()
    if c > 1 :
        break
    elif c == 0 :
        ans = 0
        break

print(ans)