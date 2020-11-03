import sys

input = sys.stdin.readline

v, e = map(int, input().rstrip().split())
node = [[] for _ in range(v + 1)]
parents = [ i for i in range(v + 1)]
edges = []

for _ in range(e) :
    a, b, c = map(int, input().rstrip().split())
    edges.append([a, b, c])

ans = 0

def find(a) :
    if parents[a] != a :
        parents[a] = find(parents[a])
        return parents[a]
    return parents[a]

for a, b, cost in sorted(edges, key = lambda x : x[2]) :
    a = find(a)
    b = find(b)

    if a == b : continue
    if a < b :
        parents[b] = parents[a]
    else : parents[a] = parents[b]

    ans += cost

print(ans)
