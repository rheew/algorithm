import sys
from collections import deque

input = sys.stdin.readline

T = int(input().rstrip())

def paint(start, node, color, visit):
    d = deque()
    d.append((start, 0))

    while d:
        now, precolor = d.popleft()

        if precolor == 1:
            precolor = 0
        else:
            precolor = 1

        for i in node[now]:
            if visit[i]: continue
            visit[i] = True
            color[i] = precolor
            d.append((i, color[i]))


def isBipartite(start, node, V, color, visit):
    d = deque()
    d.append((start, 0))

    while d:
        now, precolor = d.popleft()
        visit[now] = True
        for i in node[now]:
            if visit[i]: continue

            if color[i] == precolor : return False
            d.append((i, color[i]))

    return True

for _ in range(T) :
    V, E = map(int, input().rstrip().split())
    node = [[] for i in range(V + 1)]

    color = [0] * (V + 1)

    for _ in range(E) :
        x, y = map(int, input().rstrip().split())

        node[x].append(y)
        node[y].append(x)

    visit = [False] * (V + 1)
    for i in range(1, V + 1) :
        if visit[i] : continue
        paint(i, node, color, visit)

    flag = False
    visit = [False] * (V + 1)
    for i in range(1, V + 1) :
        if visit[i] : continue
        if not isBipartite(i, node, V, color, visit):
            flag = True
            break

    if not flag : print('YES')
    else : print('NO')