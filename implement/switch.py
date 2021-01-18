import sys

input = sys.stdin.readline

N = int(input().rstrip())

board = list(map(int, input().rstrip().split()))

people = int(input().rstrip())

def man(board, n):

    for i in range(len(board)):
        if (i + 1) % n == 0:
            board[i] = abs(board[i] - 1)

def woman(board, n):

    start = 0
    end = len(board) - 1
    n = n - 1
    back = n
    front = n

    board[n] = abs(board[n] - 1)

    while back - 1 >= start and front + 1<= end:
        back -= 1
        front += 1

        if board[back] != board[front]: break

        board[back] = abs(board[back] - 1)
        board[front] = abs(board[front] - 1)

for _ in range(people):
    sex, num = map(int,input().rstrip().split())

    if sex == 1: man(board, num)
    else: woman(board, num)

for ind, i in enumerate(board):
    print(i, end=' ')
    if (ind + 1) % 20 == 0: print()