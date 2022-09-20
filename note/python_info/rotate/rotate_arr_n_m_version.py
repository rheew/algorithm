def rotate(board):
    rlen = len(board[0])
    clen = len(board)
    x, y = 0, 0
    #위
    pre = -1
    for i in range(0, rlen) :
        now = board[x][y + i]
        board[x][y + i] = pre
        pre = now

    #오른쪽
    for i in range(1, clen):
        now = board[x + i][y + rlen - 1]
        board[x + i][y + rlen - 1] = pre
        pre = now

    #아래
    for i in range(1, rlen):
        now = board[x + clen - 1][y + rlen - 1 - i]
        board[x + clen - 1][y + rlen - 1 - i] = pre
        pre = now

    #왼쪽
    for i in range(1, clen):
        now = board[x + clen - 1 - i][y]
        board[x + clen - 1 - i][y] = pre
        pre = now
