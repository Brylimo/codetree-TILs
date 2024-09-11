import sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())
quests = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

total = sum([
    quests[i][0]
    for i in range(n)
])

dp = [INT_MAX] * (total + 1)
dp[0] = 0

for j in range(n):
    for i in range(total, -1, -1):
        if i >= quests[j][0]:
            if dp[i - quests[j][0]] == INT_MAX:
                continue

            dp[i] = min(dp[i], dp[i - quests[j][0]] + quests[j][1])

if len(dp) > m:
    ans = min(dp[m:])
    if ans == INT_MAX:
        print(-1)
    else:
        print(ans)
else:
    print(-1)