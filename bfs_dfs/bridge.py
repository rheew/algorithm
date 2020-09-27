import sys
from collections import deque

input = sys.stdin.readline
N = int(input().rstrip())

board = [list(map(int, input().rstrip().split())) for _ in range(N)]

dx, dy = [1,-1,0,0,], [0,0,-1,1]
ind = 2
min_value = int(1e9)

def find_land(x, y, ind):
    q = deque()
    q.append((x, y))
    board[x][y] = ind
    while q :
        x, y = q.popleft()

        for i in range(4) :
            nx, ny = dx[i] + x, dy[i] + y

            if nx >= N or nx < 0 or ny >= N or ny < 0 : continue
            if board[nx][ny] != 1 : continue
            board[nx][ny] = ind
            q.append((nx, ny))

    return

def find_path(a, b, ind) :
    q = deque()
    q.append((a, b, 0))
    visit = [[False] * N for _ in range(N)]
    visit[a][b] = True
    while q:
        x, y, cost = q.popleft()

        if board[x][y] != ind and board[x][y] != 0 :
            return cost - 1

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if nx >= N or nx < 0 or ny >= N or ny < 0: continue
            if board[nx][ny] == ind or visit[nx][ny]: continue
            visit[nx][ny] = True
            q.append((nx, ny, cost + 1))

    return 0

for i in range(N) :
    for j in range(N) :
        if board[i][j] != 1 : continue
        find_land(i, j, ind)
        ind += 1

for i in range(N) :
    for j in range(N) :
        if board[i][j] == 0 : continue
        result = find_path(i, j, board[i][j])

        if result == 0 : continue
        min_value = min(result, min_value)

print(min_value)


