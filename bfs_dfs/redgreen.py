from collections import deque
N = int(input())

li = [input() for _ in range(N)]

dx, dy = [1,-1,0,0], [0,0,-1,1]
visitRG = [[False for _ in range(N)] for _ in range(N)]
visitAll = [[False for _ in range(N)] for _ in range(N)]
ans1, ans2 = 0, 0

def caseRG(location):
    cnt = 1
    d = deque()
    d.append(location)
    while len(d):
        x, y = d.popleft()
        visitRG[x][y] = True
        for i in range(4):
            nextx = x + dx[i]
            nexty = y + dy[i]

            if nextx < 0 or nextx >= N or nexty < 0 or nexty >= N or visitRG[nextx][nexty]: continue
            if li[nextx][nexty] == li[x][y] or li[nextx][nexty] in 'RG' and li[x][y] in 'RG':
                d.append((nextx, nexty))
                visitRG[nextx][nexty] = True
    return cnt

def caseAll(location):
    cnt = 1
    d = deque()
    d.append(location)
    while len(d):
        x, y = d.popleft()
        visitAll[x][y] = True
        for i in range(4):
            nextx = x + dx[i]
            nexty = y + dy[i]
            if nextx < 0 or nextx >= N or nexty < 0 or nexty >= N or visitAll[nextx][nexty]: continue
            if li[nextx][nexty] == li[x][y] :
                d.append((nextx, nexty))
                visitAll[nextx][nexty] = True
    return cnt

for i in range(N):
    for j in range(N):
        if not visitRG[i][j]:
            ans1 += caseRG((i, j))
        if not visitAll[i][j]:
            ans2 += caseAll((i,j))

print(ans2, ans1)