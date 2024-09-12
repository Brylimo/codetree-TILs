import sys
INT_MIN = -sys.maxsize

n, k = map(int, input().split())
array = [0] + list(map(int, input().split()))

dp = [
    [INT_MIN] * (k + 1)
    for _ in range(n + 1)
]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(k + 1):
        if array[i] > 0:
            if dp[i - 1][j] == INT_MIN:
                continue

            dp[i][j] = max(dp[i][j], array[i])

            if dp[i - 1][j] != INT_MIN:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + array[i])
        elif array[i] < 0:
            dp[i][j] = max(dp[i][j], array[i])

            if dp[i - 1][j - 1] != INT_MIN and j >= 1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + array[i])

sum_val = max([
    dp[i][j]
    for i in range(1, n + 1)
    for j in range(k + 1)
])
print(sum_val)