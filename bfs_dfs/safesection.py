from collections import deque
N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]

maxheight = 0
for i in li:
    maxheight = max(maxheight, max(i))

dx, dy = [1,-1,0,0], [0,0,-1,1]
def checksection(visit):
    d = deque()
    sectionNum = 0

    for i, valuei in enumerate(visit):
        for j, valuej in enumerate(valuei):
            if(not visit[i][j]):
                sectionNum += 1
                d.append((i,j))

                while len(d):
                    x, y = d.popleft()
                    for l in range(4):
                        nextx = x + dx[l]
                        nexty = y + dy[l]
                        if nextx < 0 or nextx >= N or nexty < 0 or nexty >= N or visit[nextx][nexty]: continue
                        visit[nextx][nexty] = True
                        d.append((nextx,nexty))
    return sectionNum

def rain(height):
    visit = [[False for _ in range(N)] for _ in range(N)]
    for i, valuei in enumerate(li):
        for j, valuej in enumerate(valuei):
            if valuej <= height:
                visit[i][j] = True
    return checksection(visit)

answer = 0
for i in range(maxheight + 1):
    answer = max(answer, rain(i))
print(answer)
