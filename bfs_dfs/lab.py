import sys
from collections import deque
import copy
input = sys.stdin.readline

R, C = map(int, input().rstrip().split())

virus = deque()
lab = [list(map(int, input().rstrip().split())) for i in range(R)]
visit = [[False for _ in range(C)] for _ in range(R) ]

ans = 0

for i in range(R):
    for j in range(C):
        if lab[i][j] == 2 : virus.append((i,j))

def insert(y, x, temp, nlab):
    if temp == 3:
        extension(nlab)
        return

    lab = copy.deepcopy(nlab)

    for i in range(y, R):
        for j in range(C):
            if lab[i][j] == 2 or lab[i][j] == 1: continue
            lab[i][j] = 1
            insert(i, j, temp + 1, lab)
            lab[i][j] = 0

def extension(nlab):
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    nvirus = virus.copy()
    lab = copy.deepcopy(nlab)
    while len(nvirus):
        y, x = nvirus.popleft()

        for i in range(4):
            nextY, nextX = dy[i] + y, dx[i] + x

            if (nextY >= R or nextY < 0 or nextX >= C or nextX < 0): continue
            if lab[nextY][nextX] != 0: continue
            lab[nextY][nextX] = 2
            nvirus.append((nextY, nextX))

    calcul(lab)

def calcul(nlab):
    sum = 0
    global ans

    for i in range(R):
        sum += nlab[i].count(0)

    ans = max(ans, sum)

insert(0, 0, 0, lab)
print(ans)
