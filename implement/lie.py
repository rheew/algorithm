import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

know = list(map(int, input().rstrip().split()))
know = set(know[1:])

node = [[] for _ in range(N + 1)]
partys = []
for _ in range(M) :
    party = list(map(int, input().rstrip().split()))
    partys.append(party)
    for x, y in list(combinations(party[1:], 2)) :
        node[x].append(y)
        node[y].append(x)

def BFS() :
    q = deque()
    visit = [False] * (N + 1)
    for i in list(know) :
        q.append(i)

    while q :
        now = q.popleft()

        for i in node[now] :
            if visit[i] : continue
            visit[i] = True
            q.append(i)
            know.add(i)

BFS()
ans = 0
for party in partys :
    flag = True
    for i in party[1:] :
        if i in know :
            flag = False
            break

    if flag : ans += 1

print(ans)
