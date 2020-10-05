import sys
from collections import deque

input = sys.stdin.readline

T = int(input().rstrip())
def BFS(start, node, visit, degree) :
    d = deque()
    d.append(start)
    cnt = 0

    while d :
        now = d.popleft()
        visit[now] = True
        cnt += 1
        parents = node[now]
        degree[parents] -= 1

        if degree[parents] == 0 :
            d.append(parents)

    return cnt

for _ in range(T) :
    N = int(input().rstrip())
    people = list(map(int, input().rstrip().split()))
    people.insert(0,0)

    degree = [0] * (N + 1)
    ans = 0
    visit = [False] * (N + 1)

    for i in range(1, N + 1) :
        parents = people[i]
        degree[parents] += 1

    for i in range(1, N + 1) :
        if visit[i]: continue

        if degree[i] == 0:
            ans += BFS(i, people, visit, degree)

    print(ans)