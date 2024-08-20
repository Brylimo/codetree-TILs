n, m = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dir = 2
grid = [[0] * m for _ in range(n)]

num = 1
x, y = 0, 0
while True:
    grid[x][y] = num

    if num == n * m:
        break

    num += 1
    nx = x + dx[dir]
    ny = y + dy[dir]

    if (nx < 0 or nx >= n or ny < 0 or ny >= m) or grid[nx][ny] != 0:
        dir = (dir + 3) % 4

        x = x + dx[dir]
        y = y + dy[dir]
        continue

    x, y = nx, ny

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()