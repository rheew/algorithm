import sys
from collections import deque

input = sys.stdin.readline

x, y = map(int, input().rstrip().split())

start = 1
end = x * 2
pre = int(100 * y / x)
ans = -1

while start <= end:
    mid = ( start + end )// 2
    now = int(100 * (y + mid) / (x + mid))

    if now != pre:
        end = mid - 1
        ans = mid

    else:
        start = mid + 1

print(ans)