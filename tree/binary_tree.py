import sys
from collections import deque

input = sys.stdin.readline

k = int(input().rstrip())
visit = list(map(int, input().rstrip().split()))

node = [[] for _ in range(k)]
def preorder(visit, hei):
    if not len(visit) or hei == k: return

    mid = len(visit) // 2
    node[hei].append(visit[mid])
    preorder(visit[0:mid], hei + 1)
    preorder(visit[mid:], hei + 1)

preorder(visit, 0)

for i in node:
    for j in i:
        print(j, end=' ')
    print()