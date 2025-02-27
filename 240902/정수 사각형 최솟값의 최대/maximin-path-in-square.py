n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [0] * n
    for _ in range(n)
]

def initialize():
    dp[0][0] = grid[0][0]
    # 첫번째 열
    for i in range(1, n):
        if dp[i - 1][0] > grid[i][0]:
            dp[i][0] = grid[i][0]
        else:
            dp[i][0] = dp[i - 1][0]

    # 첫번째 행
    for i in range(1, n):
        if dp[0][i - 1] > grid[0][i]:
            dp[0][i] = grid[0][i]
        else:
            dp[0][i] = dp[0][i - 1]

def show():
    for i in range(n):
        print(dp[i])

initialize()

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(max(dp[i - 1][j], dp[i][j - 1]), grid[i][j])

print(dp[n - 1][n - 1])