import sys

INT_MAX = sys.maxsize

n, m = map(int, input().split())
seq = [0] + list(map(int, input().split()))

dp = [INT_MAX] * (m + 1)
dp[0] = 0

for i in range(1, n + 1):
    for j in range(m, -1, -1):
        if seq[i] <= j:
            dp[j] = min(dp[j], dp[j - seq[i]] + 1)

if dp[m] == INT_MAX:
    print(-1)
else:
    print(dp[m])