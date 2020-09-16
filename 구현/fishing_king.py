import sys
from collections import deque

input = sys.stdin.readline

R, C, M = map(int, input().rstrip().split())

shark = [list(map(int, input().rstrip().split())) for _ in range(M)]
board = [[0] * (C + 1) for _ in range(R + 1)]
people = -1
sharkq = deque()

for i in shark :
    sharkq.append(i)

dr, dc = [0,-1,1,0,0], [0,0,0,1,-1] # d : 1 위 2 아래  3  오른쪽 4 왼쪽

def sharkMove() :
    sharknum = len(sharkq)

    for _ in range(sharknum) :
        r, c, s, d, z = sharkq.popleft()
        nr, nc = r, c
        for i in range(s) :
            nr, nc = nr + dr[d], nc + dc[d]

            if nr > R or nr <= 0 or nc > C or nc <= 0 :
                nr, nc = nr - dr[d], nc - dc[d]

                if d % 2 == 0 : d -= 1
                else : d += 1

                nr, nc = nr + dr[d], nc + dc[d]
        sharkq.append((nr,nc,s,d,z))

        board[nr][nc] = max(board[nr][nc], z)

    return

def sharkEat() :
    sharknum = len(sharkq)
    for i in range(sharknum) :
        r, c, s, d, z = sharkq.popleft()
        if board[r][c] != z : continue
        sharkq.append((r, c, s, d, z))

    for i in range(R + 1):
        for j in range(C + 1):
            board[i][j] = 0

    return

def getShark(people) :
    value = 0
    sharknum = len(sharkq)

    for i in range(sharknum) :
        r, c, s, d, z = sharkq.popleft()
        board[r][c] = z
        sharkq.append((r, c, s, d, z))

    for i in range(1, R + 1) :
        if board[i][people] != 0 :
            value += board[i][people]
            board[i][people] = 0
            break

    for i in range(sharknum) :
        r, c, s, d, z = sharkq.popleft()
        if board[r][c] == 0 : continue
        board[r][c] = 0
        sharkq.append((r, c, s, d, z))

    return value

def game(people) :
    ans = 0
    while people < C :
        people += 1
        ans += getShark(people)
        sharkMove()
        sharkEat()

    return ans

print(game(0))