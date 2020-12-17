import sys

input = sys.stdin.readline

N = int(input().rstrip())

board = [list(map(int, input().rstrip().split())) for _ in range(N)]

def find(node, visit):
    result = []

    for i in range(N):
        if node == i or visit[i]: continue

        if board[node][i] == 1 : result.append(i)

    return result

for i in range(N):
    visit = [False] * N

    for j in range(N):
        if visit[j]: continue

        result = []

        if board[i][j] == 1:
            result = find(j, visit)

        while result:

            k = result[0]
            del result[0]

            if visit[k] : continue
            visit[k] = True
            board[i][k] = 1
            result.extend(find(k, visit))

for i in range(N):
    for j in range(N):
        print(board[i][j], end=' ')
    print()
