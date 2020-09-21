import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]
dx, dy = [0,0,1,-1], [1,-1,0,0]

def air(x, y) :
    d = deque()
    d.append((x,y))
    board[x][y] = 2
    while d :
        x, y = d.popleft()
        for i in range(4) :
            nx, ny = dx[i] + x, dy[i] + y
            if nx < 0 or nx >= N or ny < 0 or ny >= M : continue
            if board[nx][ny] : continue
            board[nx][ny] = 2
            d.append((nx,ny))

    return

def ismelt(x, y):
    cnt = 0

    for i in range(4) :
        nx, ny = dx[i] + x, dy[i] + y
        if board[nx][ny] == 2 :
            cnt += 1
    if cnt > 1 : return True
    else : return False

def melt(cheese) :
    while cheese :
        x, y = cheese.popleft()
        board[x][y] = 2

    return

def checkmelt():
    meltcheese = deque()

    for i in range(N) :
        for j in range(M) :
            if board[i][j] == 1 and ismelt(i, j) :
                meltcheese.append((i, j))

    if not meltcheese : return False
    melt(meltcheese)
    return True

def isair(x, y):
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if board[nx][ny] == 2: return True

    return False

def game():
    cnt = 0
    while checkmelt() :
        cnt += 1
        for i in range(N) :
            for j in range(M) :
                if board[i][j] == 0 and isair(i,j):
                    air(i,j)

    return cnt

air(0,0)
print(game())