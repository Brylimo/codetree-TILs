import sys
INT_MIN = -sys.maxsize

n = int(input())
stairs = list(map(int, input().split()))

dp = [
    [INT_MIN for _ in range(4)]
    for _ in range(n + 1)
]
dp[0][0] = 0

for i in range(1, n + 1):
    if dp[i - 2][0] != INT_MIN:
        dp[i][0] = dp[i - 2][0] + stairs[i - 1]
    if dp[i - 1][0] != INT_MIN or dp[i - 2][1] != INT_MIN:
        dp[i][1] = max(dp[i - 1][0], dp[i - 2][1]) + stairs[i - 1]
    if dp[i - 1][1] != INT_MIN or dp[i - 2][2] != INT_MIN: 
        dp[i][2] = max(dp[i - 1][1], dp[i - 2][2]) + stairs[i - 1]
    if dp[i - 1][2] != INT_MIN or dp[i - 2][3] != INT_MIN:
        dp[i][3] = max(dp[i - 1][2], dp[i - 2][3]) + stairs[i - 1]

print(max(dp[n]))