n = int(input())
grid = [[0] * n for _ in range(n)]

num = 1
x, y = n // 2, n // 2

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = 1
while True:
    grid[x][y] = num

    if grid[x][y] == n * n:
        break

    num += 1
    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        dir = (dir + 3) % 4
        x = x + dx[dir]
        y = y + dy[dir]
        continue

    cnt = 0
    for i in range(4):
        px = nx + dx[i]
        py = ny + dy[i]

        if px < 0 or px >= n or py < 0 or py >= n:
            continue

        if grid[px][py] == 0:
            cnt += 1
    
    if cnt == 3:
        dir = (dir + 3) % 4
        x = nx
        y = ny
        continue
    else:
        x = nx
        y = ny

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()