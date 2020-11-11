import sys
input = sys.stdin.readline

N = int(input().rstrip())

board = [list(map(int, input().rstrip().split())) for _ in range(N)]

minDp = board[0].copy()
maxDp = board[0].copy()

for i in range(1, N):
    jmin = [0,0,0]
    jmax = [0,0,0]

    jmin[0] = board[i][0] + min(minDp[0], minDp[1])
    jmin[1] = board[i][1] + min(minDp[0], minDp[1], minDp[2])
    jmin[2] = board[i][2] + min(minDp[1], minDp[2])

    jmax[0] = board[i][0] + max(maxDp[0], maxDp[1])
    jmax[1] = board[i][1] + max(maxDp[0], maxDp[1], maxDp[2])
    jmax[2] = board[i][2] + max(maxDp[1], maxDp[2])

    maxDp = jmax
    minDp = jmin

print(max(maxDp), min(minDp))