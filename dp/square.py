import sys
import math

input = sys.stdin.readline

N, M= map(int, input().rstrip().split())

board = [[int(j) for j in input().rstrip()] for _ in range(N)]
ans = 0
for i in range(1, N) :
    for j in range(1, M) :
        if board[i][j] > 0 and board[i][j-1] > 0 and board[i-1][j] > 0 and board[i-1][j-1] > 0 :
            value = min(board[i-1][j], board[i][j-1], board[i-1][j-1])
            board[i][j] = int(math.sqrt(value) + 1) ** 2
            ans = max(board[i][j], ans)
if N == 1 : ans = 1
print(ans)