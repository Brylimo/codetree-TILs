n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [0] * m
    for _ in range(n)
]

dp[0][0] = 1
for i in range(1, n):
    for j in range(1, m):
        for a in range(i):
            for b in range(j):
                if dp[a][b] == 0:
                    continue

                if grid[a][b] < grid[i][j]:
                    dp[i][j] = max(dp[i][j], dp[a][b] + 1)

ans = max([
    dp[i][j]
    for i in range(n)
    for j in range(m)
])

print(ans)