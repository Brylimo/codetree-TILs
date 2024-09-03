import sys

INT_MAX = sys.maxsize

n, m = map(int, input().split())
coins = list(map(int, input().split()))
dp = [INT_MAX] * (m + 1)
dp[0] = 0

for i in range(1, m + 1):
    for j in range(n):
        if coins[j] <= i:
            dp[i] = min(dp[i], dp[i - coins[j]] + 1)

ans = dp[m]
if ans == INT_MAX:
    print(-1)
else:
    print(ans)