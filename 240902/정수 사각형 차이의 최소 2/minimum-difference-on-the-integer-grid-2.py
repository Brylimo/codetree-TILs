n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [[0, 0] for _ in range(n)]
    for j in range(n)
]

def initialize():
    dp[0][0][0], dp[0][0][1] = grid[0][0], grid[0][0]
    
    # 첫번째 행 초기화
    for i in range(1, n):
        dp[0][i][0] = min(dp[0][i - 1][0], grid[0][i])
        dp[0][i][1] = max(dp[0][i - 1][1], grid[0][i])

    # 첫번째 열 초기화
    for i in range(1, n):
        dp[i][0][0] = min(dp[i - 1][0][0], grid[i][0])
        dp[i][0][1] = max(dp[i - 1][0][1], grid[i][0])

def show():
    for i in range(n):
        print(dp[i])

initialize()

for i in range(1, n):
    for j in range(1, n):
        up_min = min(dp[i - 1][j][0], grid[i][j])
        up_max = max(dp[i - 1][j][1], grid[i][j])

        left_min = min(dp[i][j - 1][0], grid[i][j])
        left_max = max(dp[i][j - 1][1], grid[i][j])

        if up_max - up_min < left_max - left_min:
            dp[i][j][0] = up_min
            dp[i][j][1] = up_max
        elif up_max - up_min == left_max - left_min:
            dp[i][j][0] = up_min
            dp[i][j][1] = up_max
        else:
            dp[i][j][0] = left_min
            dp[i][j][1] = left_max

print(dp[n - 1][n - 1][1] - dp[n - 1][n - 1][0])