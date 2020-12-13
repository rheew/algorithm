import sys

input = sys.stdin.readline

col, row = map(int, input().rstrip().split())
N = int(input().rstrip())

stores = []
pos = [0, row, 0, col]
# 1 2 3 4 북 남 (왼쪽) 서 동 (위쪽)
for _ in range(N + 1):
    a, b = map(int, input().rstrip().split())
    if a == 1 or a == 2:
        stores.append([pos[a - 1], b])
    else :
        stores.append([b, pos[a - 1]])

start = stores[-1]
del stores[-1]

def distanceNorthAndSouth(store):
    y1, x1 = start
    y2, x2 = store
    minValue = 0

    if y1 == 0 or y1 == row :
        minValue = min((x1 + x2), (2 * col - x1 - x2)) + row
        if y1 == y2 :
            minValue = abs(x1 - x2)

    else :
        minValue = abs(y1 - y2)
        if x1 == 0:
            minValue += x2
        else : minValue += col - x2

    return minValue

def distanceWestAndEast(store):
    y1, x1 = start
    y2, x2 = store
    minValue = 0

    if x1 == 0 or x1 == col :
        minValue =  min((y1 + y2), (2 * row - y1 - y2)) + col
        if x1 == x2 :
            minValue = abs(y1 - y2)

    else :
        minValue = abs(x1 - x2)
        if y1 == 0:
            minValue += y2
        else : minValue += row - y2


    return minValue

ans = 0

for store in stores:
    if store[0] == 0 or store[0] == row:
        ans += distanceNorthAndSouth(store)

    else : ans += distanceWestAndEast(store)

print(ans)