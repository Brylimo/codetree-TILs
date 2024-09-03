n = int(input())
lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
dp = [1] * n

lines.sort(key = lambda x: x[1])

for i in range(n):
    for j in range(i):
        xi1, xi2 = lines[i]
        xj1, xj2 = lines[j]

        # 겹치지 않음
        if xj2 < xi1:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))