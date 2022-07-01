from collections import deque

def solution(rows, columns, queries):
    answer = []
    board = makeBoard(rows, columns)

    for query in queries:
        x1, y1, x2, y2 = query
        start, end = (x1 - 1, y1 - 1), (x2 - 1, y2 - 1)

        board, minValue = turnBoard(start, end, board)
        answer.append(minValue)

    return sorted(answer)

def turnBoard(start, end, board):

    indices = findIndex(start, end)
    q = deque()

    for i in indices:
        x, y = i

        q.append(board[x][y])

    minValue = min(q)
    q.rotate(1)

    for i in indices:
        x, y = i
        board[x][y] = q.popleft()

    return board, minValue

def right(start, end):

    return [(start[0], i) for i in range(start[1], end[1] + 1)]

def up(start, end):

    return [(i, start[1]) for i in range(end[0] - 1, start[0], -1)]

def down(start, end):

    return [(i, end[1]) for i in range(start[0] + 1, end[0] + 1)]

def left(start, end):

    return [(end[0], i) for i in range(end[1] - 1, start[1] - 1, -1)]

def findIndex(start, end):

    return right(start, end) + down(start, end) + left(start, end) + up(start, end)

def makeBoard(rowLen, columLen):

    return [[i + (j * columLen) + 1 for i in range(columLen)] for j in range(rowLen)]

r = 6
c = 5

q = 	[[1,1,5, 5]]

print(solution(r, c, q))