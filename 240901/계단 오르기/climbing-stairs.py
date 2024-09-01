DIVIDER = 10007

n = int(input())

dp = [0] * 1001
dp[2] = 1
dp[3] = 1

for i in range(4, n+1):
    dp[i] = (dp[i - 2] % DIVIDER + dp[i - 3] % DIVIDER) % DIVIDER

print(dp[n])