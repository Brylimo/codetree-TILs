MOD = 10007
n = int(input())

nums = [1, 2, 5]
dp = [0] * (n + 1)

dp[1], dp[2], dp[5] = 1, 1, 1

for i in range(1, n + 1):
    for j in range(3):
        if nums[j] <= i:
            dp[i] += dp[i - nums[j]]

print(max(dp) % MOD)