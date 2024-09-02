n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [1] * m
    for _ in range(n)
]

for i in range(n):
    for j in range(m):

        for a in range(i):
            for b in range(j):
                if grid[a][b] < grid[i][j]:
                    dp[i][j] = max(dp[i][j], dp[a][b] + 1)

ans = max([
    dp[i][j]
    for i in range(n)
    for j in range(m)
])

print(ans)