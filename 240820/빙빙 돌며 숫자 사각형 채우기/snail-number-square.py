n, m = map(int, input().split())

grid = [[0] * m for _ in range(n)]

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
x, y = 0, 0
dir = 1

grid[0][0] = 1
num = 2
while num <= n * m:
    nx = x + dx[dir]
    ny = y + dy[dir]

    if (nx < 0 or nx >= n or ny < 0 or ny >= m) or grid[nx][ny] != 0:
        dir = (dir + 3) % 4
        continue
    else:
        grid[nx][ny] = num
        num += 1

        x = nx
        y = ny

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()