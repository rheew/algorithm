import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [0,0,-1,1,-1,1,-1,1], [1,-1,0,0,1,1,-1,-1]

def BFS(board, visit, start, w, h):
    q = deque()
    q.append(start)
    # 큐를 이용해 BFS를 동작할 것이다. 초기 방문해주기
    visit[start[0]][start[1]] = True

    while q:
        y, x = q.popleft()

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= w or ny >= h : continue
            if visit[ny][nx] or board[ny][nx] == 0: continue
            visit[ny][nx] = True
            q.append([ny,nx])


while(True):
    w, h = map(int, input().rstrip().split())
    if w == h == 0 : break
    # 보드 입력을 받는다. 비짓 생성
    board = []
    visit = [[False] * w for _ in range(h)]

    for i in range(h):
        board.append(list(map(int,input().rstrip().split())))

    ans = 0

    # 2차원 포룹을 이용해 보드 하나씩 접근한다. 만약 방문하지 않은 땅이 있다면 방문해 BFS 동작한다.

    for i in range(h):
        for j in range(w):
            if board[i][j] == 0 or visit[i][j] : continue
            ans += 1

            BFS(board, visit, [i, j], w, h)

    print(ans)