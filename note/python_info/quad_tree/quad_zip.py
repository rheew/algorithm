ans = [0, 0]
def tree(board, start, end):
    global ans
    init = board[start[0]][start[1]]
    flag = False
    
    for i in range(start[0], end[0]):
        for j in range(start[1], end[1]):
            if init == board[i][j] : continue
            flag = True
            tree(board, start, [(end[0] + start[0])//2, (end[1] + start[1]) //2])
            tree(board, [start[0], (start[1] + end[1])//2], [(end[0] + start[0])//2, end[1]])
            tree(board, [(start[0] + end[0])//2, start[1]], [end[0], (end[1] + start[1]) //2])
            tree(board, [(start[0]+end[0]) // 2, (start[1] + end[1]) // 2], end)
            return
        
    if not flag:
        ans[init] += 1

def solution(arr):
    tree(arr, [0,0], [len(arr), len(arr)])
    return ans