import sys

input = sys.stdin.readline

N = int(input().rstrip())

numbers = list(map(int, input().rstrip().split()))
dp = [1] * N

for i in range(N) :
    for j in range(i + 1, N) :
        if numbers[i] < numbers[j] :
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))
