from collections import deque

dx, dy = [0,0,1,-1], [1,-1,0,0]

def BFS(maps, start):
    n = len(maps)
    m = len(maps[0])
    q = deque()
    ans = -1
    visit = [[False] * m for _ in range(n)]
    start.append(1)
    q.append(start)
    
    while q:
        x, y, cost = q.popleft()

        if x == m - 1 and y == n - 1:
            ans = cost
            break
            
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            
            if nx < 0 or ny < 0 or nx >= m or ny >= n: continue
            if visit[ny][nx] or maps[ny][nx] == 0: continue
                
            visit[ny][nx] = True
            q.append([nx, ny, cost + 1])
    
    return ans

def solution(maps):
    answer = BFS(maps, [0,0])
    return answer