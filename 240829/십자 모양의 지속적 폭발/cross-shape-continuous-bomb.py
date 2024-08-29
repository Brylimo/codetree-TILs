n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cols = []
for _ in range(m):
    cols.append(int(input()))

def bomb(x, y):
    # 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0

    bomb_range = grid[x][y]

    # bomb
    for i in range(n):
        for j in range(n):
            if (i == x or j == y) and abs(x - i) + abs(y - j) < bomb_range:
                grid[i][j] = 0

    # gravity
    for j in range(n):
        end_of_temp = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j] != 0:
                next_grid[end_of_temp][j] = grid[i][j]
                end_of_temp -= 1

    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

for col in cols:
    for row in range(n):
        if grid[row][col - 1] != 0:
            bomb(row, col - 1)
            break

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()