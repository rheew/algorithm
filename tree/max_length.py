import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().rstrip())

node = [[] for _ in range(N+1)]
cost = [0] * (N + 1)

for _ in range(N-1) :
    x, y, c = map(int, input().rstrip().split())

    node[x].append(y)
    cost[y] = c

ans = 0
def find(num):
    global ans

    h = []
    for i in node[num] :
        temp = find(i)
        heapq.heappush(h, -temp)

    cnt = 0
    totalsum = 0
    maxvalue = 0
    while h :
        if cnt == 2 : break
        cnt += 1
        value = -heapq.heappop(h)
        totalsum += value
        maxvalue = max(maxvalue, value)

    ans = max(ans, totalsum)
    return maxvalue + cost[num]

find(1)
print(ans)