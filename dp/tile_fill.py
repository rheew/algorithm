import sys
input = sys.stdin.readline

N = int(input().rstrip())

dp = [0] * (N + 2)
dp[2] = 3

for i in range(4, N + 1):
    if i % 2 != 0: continue

    result = dp[i - 2] * 3

    for j in range(2, i - 3):
        result += dp[j] * 2
    dp[i] = result + 2

print(dp[N])