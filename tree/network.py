import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())
edges = []
nodes = [i for i in range(N + 1)]

for _ in range(K) :
    a, b, cost = map(int, input().rstrip().split())
    edges.append([a,b,cost])

def union(a, b) :
    a = find(a)
    b = find(b)

    if a == b : return False

    if a > b : nodes[b] = a
    else : nodes[a] = b
    return True

def find(a) :
    if nodes[a] != a :
        nodes[a] = find(nodes[a])
    return nodes[a]

ans = 0
for a, b, cost in sorted(edges, key = lambda x : x[2]) :
    if union(a, b) :
        ans += cost

print(ans)