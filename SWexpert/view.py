for t in range(10):

    bottom = int(input())
    height = list(map(int,input().split()))

    dp = [0] * bottom
    ans = 0

    for i in range(bottom - 2):
        dp[i + 1] = max(height[i], dp[i + 1])
        dp[i + 2] = max(height[i], dp[i + 2])

    for i in range(bottom - 1, 1, -1):
        dp[i - 1] = max(height[i], dp[i - 1])
        dp[i - 2] = max(height[i], dp[i - 2])

    for i in range(bottom):
        if height[i] > dp[i]:
            ans += height[i] - dp[i]

    print("#"+str(t+1),ans)