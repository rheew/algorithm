import sys
from collections import Counter

input = sys.stdin.readline
r, c, k = map(int, input().rstrip().split())

board = [list(map(int, input().rstrip().split())) for _ in range(3)]

time = 0
rlen = 3
clen = 3

def roperation(board):
    nboard = []
    maxlen = 0


    for i in board :
        nr = []
        zero = 0
        count_num = Counter(i)
        count_num = sorted(count_num.items(), key=lambda x : (x[1],x[0]))
        for x, y in count_num :
            if x == 0 :
                zero += 1
                continue

            nr.extend([x,y])

        maxlen = max(len(nr), maxlen)
        for i in range(zero):
            nr.append(0)

        nboard.append(nr)

    for i in range(len(nboard)) :

        while maxlen > len(nboard[i]) :
            nboard[i].append(0)

        while maxlen < len(nboard[i]) :
            del nboard[i][-1]

    return nboard

def turnBoard(board) :
    board = [list(i) for i in zip(*board)]
    return board

while time <= 100 :
    rlen = len(board)
    clen = len(board[0])

    if r <= rlen and c <= clen :
        if board[r-1][c-1] == k : break

    if rlen >= clen :
        board = roperation(board)
    else :
        board = turnBoard(board)
        board = roperation(board)
        board = turnBoard(board)

    time += 1

if time == 101 : print(-1)
else : print(time)
