from collections import deque


def solution(rows, columns, queries):
    answer = []

    board = [[(i * columns) + j + 1 for j in range(columns)] for i in range(rows)]

    for x1, y1, x2, y2 in queries:
        # 우 하 좌 상
        values = []

        pre = 0

        # 우
        for i in range(y1 - 1, y2):
            temp = board[x1 - 1][i]
            board[x1 - 1][i] = pre
            pre = temp
            values.append(temp)
        # 하
        for i in range(x1, x2):
            temp = board[i][y2 - 1]
            board[i][y2 - 1] = pre
            pre = temp
            values.append(temp)
        # 좌
        for i in range(y2 - 2, y1 - 2, -1):
            temp = board[x2 - 1][i]
            board[x2 - 1][i] = pre
            pre = temp
            values.append(temp)

        # 상
        for i in range(x2 - 2, x1 - 2, -1):
            temp = board[i][y1 - 1]
            board[i][y1 - 1] = pre
            pre = temp
            values.append(temp)
        del values[-1]
        answer.append(min(values))

    return answer