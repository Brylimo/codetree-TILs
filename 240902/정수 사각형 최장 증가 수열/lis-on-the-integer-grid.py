n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [1] * n
    for _ in range(n)
]

orders = []
for i in range(n):
    for j in range(n):
        orders.append((grid[i][j], i, j))

orders.sort(reverse = True)

def get_counts(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if grid[nx][ny] < grid[x][y]:
            dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)

for order in orders:
    num, x, y = order
    get_counts(x, y)

ans = max([
    dp[i][j]
    for i in range(n)
    for j in range(n)
])

print(ans)