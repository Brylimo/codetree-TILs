import sys
INT_MIN = -sys.maxsize

n, m = map(int, input().split())
diamonds = []
for _ in range(n):
    diamonds.append(tuple(map(int, input().split())))
    
dp = [INT_MIN] * (m + 1)
dp[0] = 0

for i in range(m + 1):
    for j in range(n):
        if diamonds[j][0] <= i:
            if dp[i - diamonds[j][0]] == INT_MIN:
                continue

            dp[i] = max(dp[i], dp[i - diamonds[j][0]] + diamonds[j][1])

print(max(dp))