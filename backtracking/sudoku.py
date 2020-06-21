import sys
input = sys.stdin.readline

zero = []
li = [input().split() for _ in range(9)]
for ind, i in enumerate(li):
    for jind, j in enumerate(i):
        if(j == '0'):
            zero.append((ind, jind))

def DFS(li, temp, zero):
    if temp == len(zero):
        for i in li:
            for j in range(9):
                print(i[j], end=' ')
            print()
        exit()
        return

    y, x = zero[temp]
    visit = [False for _ in range(10)]

    startY = int(y / 3) * 3
    startX = int(x / 3) * 3
    for Y in range((startY), (startY) + 3):
        for X in range((startX), (startX) + 3):
            visit[int(li[Y][X])] = True

    for i in range(9):
        visit[int(li[i][x])] = True
        visit[int(li[y][i])] = True

    for i in range(1, 10):
        if visit[i]: continue
        li[y][x] = str(i)
        DFS(li, temp+1, zero)
        li[y][x] = 0

DFS(li, 0, zero)