import sys

INT_MIN = -sys.maxsize

n = int(input())
stick = [0] + list(map(int, input().split()))

dp = [INT_MIN] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i >= j:
            if dp[i - j] == INT_MIN:
                continue

            dp[i] = max(dp[i], dp[i - j] + stick[j])

print(max(dp))