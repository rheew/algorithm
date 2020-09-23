import sys
from itertools import permutations
import copy

input = sys.stdin.readline
N, M, K = map(int, input().rstrip().split())

board = [list(map(int, input().rstrip().split())) for _ in range(N)]
opers = [list(map(int, input().rstrip().split())) for _ in range(K)]

def turn(blen, x, y, board):
    #위
    pre = -1
    for i in range(0, blen) :
        now = board[x][y + i]
        board[x][y + i] = pre
        pre = now

    #오른쪽
    for i in range(1, blen):
        now = board[x + i][y + blen - 1]
        board[x + i][y + blen - 1] = pre
        pre = now

    #아래
    for i in range(1, blen):
        now = board[x + blen - 1][y + blen - 1 - i]
        board[x + blen - 1][y + blen - 1 - i] = pre
        pre = now

    #왼쪽
    for i in range(1, blen):
        now = board[x + blen - 1 - i][y]
        board[x + blen - 1 - i][y] = pre
        pre = now

def cntValue(board):
    blen = len(board)
    min_value = int(1e9)
    for i in range(blen):
        min_value = min(sum(board[i]), min_value)

    return min_value

def game():
    ans = int(1e10)

    for pick in list(permutations(opers, K)) :

        nboard = copy.deepcopy(board)
        for r, c, s in pick :
            start = (r - s - 1, c - s - 1)
            end = (r + s - 1, c + s - 1)
            blen = end[0] - start[0] + 1

            while 1 < blen :
                turn(blen, start[0],start[1], nboard)
                start = (start[0] + 1, start[1] + 1)
                blen -= 2

        ans = min(ans, cntValue(nboard))

    return ans

print(game())
