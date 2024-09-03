import sys

INT_MIN = -sys.maxsize

n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [INT_MIN] * (m + 1)
dp[0] = 0
for i in range(1, m + 1):
    for j in range(n):
        if coins[j] <= i:
            if dp[i - coins[j]] == INT_MIN:
                continue

            dp[i] = max(dp[i], dp[i - coins[j]] + 1)

ans = dp[m]
if ans == INT_MIN:
    print(-1)
else:
    print(dp[m])