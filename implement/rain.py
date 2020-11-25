import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
board = list(map(int, input().rstrip().split()))

left = 0
right = 1

def cnt(left, right, hei):
    total = 0
    for i in range(left + 1, right):
        total += hei - board[i]

    return total

ans = 0

while left < M - 1:
    maxhei = board[left]
    sechei = left + 1
    for i in range(left + 1, M):
        if board[i] > maxhei:
            ans += cnt(left, i, board[left])
            left = i
            break

        if board[i] > board[sechei]:
            sechei = i

        if i == M - 1:
            ans += cnt(left, sechei, board[sechei])
            left = sechei
            break

print(ans)