from collections import deque
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

posX, posY = 0, 0
waterD = deque()
ansX, ansY = 0, 0
city = [[i for i in input().rstrip()] for _ in range(N)]
visit = [[-1 for _ in range(M)] for _ in range(N)]
dx, dy = [0,0,-1,1], [-1,1,0,0]

for ind, i in enumerate(city):
    for indj, j in enumerate(i) :
        if j == 'S' :
            posY, posX = ind, indj
        if j == '*' :
            waterD.append((ind, indj))
        if j == 'D' :
            ansX, ansY = indj, ind

def moveWater(water, city):
    moveTime = len(water)

    for i in range(moveTime):
        waterY, waterX = water.popleft()

        for j in range(4):
            nextY, nextX = dy[j] + waterY, dx[j] + waterX
            if nextX >= M or nextX < 0 or nextY >= N or nextY < 0: continue
            if city[nextY][nextX] != '.' : continue
            water.append((nextY,nextX))
            city[nextY][nextX] = '*'
    return water

def BFS(x, y, city, waterD):
    d = deque()
    d.append((x,y,city,waterD))
    while(len(d)):
        x, y, city, waterD = d.popleft()

        if city[y][x] == 'D':
            return
        ncity = copy.deepcopy(city)
        nwaterD = waterD.copy()
        nwaterD = moveWater(nwaterD, ncity)

        for i in range(4):
            nextY, nextX = dy[i]+y, dx[i]+x

            if nextX >= M or nextX < 0 or nextY >= N or nextY < 0 : continue
            if ncity[nextY][nextX] == '*' or ncity[nextY][nextX] == 'X' : continue

            if visit[nextY][nextX] != -1:
                if visit[nextY][nextX] > visit[y][x] + 1 :
                    visit[nextY][nextX] = visit[y][x] + 1
                    ncity[nextY][nextX] = 'S'
                    ncity[y][x] = '.'
                    d.append((nextX, nextY, ncity, nwaterD))
                    ncity[nextY][nextX] = '.'
                    ncity[y][x] = 'S'
            else :
                visit[nextY][nextX] = visit[y][x] + 1
                ncity[nextY][nextX] = 'S'
                ncity[y][x] = '.'
                d.append((nextX, nextY, ncity, nwaterD))
                ncity[nextY][nextX] = '.'
                ncity[y][x] = 'S'

visit[posY][posX] = 0
BFS(posX, posY, city, waterD)
if visit[ansY][ansX] == -1 : print('KAKTUS')
else : print(visit[ansY][ansX])