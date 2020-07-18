def isFour(block, x, y):
    if len(block[x+1]) < y + 2: return False
    
    if  block[x][y] == block[x][y+1] and block[x][y] == block[x+1][y] and block[x][y] == block[x+1][y+1]:
        return  True
    return False

def deleteBlock(block, visit, n, m):
    flag = False
    cnt = 0
    
    for i in range(n):
        for j in range(len(block[i]) - 1, -1, -1):
            if visit[i][j]:
                flag = True
                cnt += 1
                del block[i][j]

    return flag, cnt
    
def solution(m, n, board):
    answer = 0
    board = [list(reversed(i)) for i in zip(*board)]
    
    while(True):
        visit = [[False for _ in range(m)] for _ in range(n)]
        
        for i in range(n-1):
            for j in range(len(board[i]) - 1):
                if isFour(board, i,j):
                    visit[i][j] = visit[i+1][j] = visit[i][j+1] = visit[i+1][j+1] = True

        oper, cnt = deleteBlock(board, visit, n, m)
        if not oper :break
        answer += cnt
    return answer