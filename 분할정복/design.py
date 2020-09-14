import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input().rstrip())
num = list(map(int, input().rstrip().split()))
dp = []
for i in num:
    ind = bisect_left(dp, i)
    if ind >= len(dp) :
        dp.append(i)
    else : dp[ind] = i

print(len(dp))