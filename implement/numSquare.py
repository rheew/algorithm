import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
board = []
for i in range(N):
    board.append([i for i in input().rstrip()])

ans = 1

for i in range(N - 1):
    for j in range(M - 1):
        minValue = min(N - i, M - j)

        for k in range(1, minValue):

            if board[i][j] == board[i + k][j + k] == board[i][j + k] == board[i + k][j] :
                ans = max(ans, (k + 1) * (k + 1))

print(ans)