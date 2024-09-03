import sys
INT_MIN = -sys.maxsize
n, m = map(int, input().split())

jwerlies = []
for _ in range(n):
    w, v = map(int, input().split())
    jwerlies.append((w, v))

dp = [INT_MIN] * (m + 1)
dp[0] = 0

for j in range(n):
    for i in range(m, -1, -1):
        if i >= jwerlies[j][0]:
            if dp[i - jwerlies[j][0]] == INT_MIN:
                continue

            dp[i] = max(dp[i], dp[i - jwerlies[j][0]] + jwerlies[j][1])

print(dp[m])