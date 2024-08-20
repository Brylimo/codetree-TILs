n, m = map(int, input().split())

grid = [[0] * m for _ in range(n)]

dx = [-1, 0, 1 ,0]
dy = [0, 1, 0, -1]

dir = 1
cnt = 1
num = ord('A')
x, y = 0, 0
while True:
    grid[x][y] = chr(num)

    if cnt == n * m:
        break

    cnt += 1
    if num == ord('Z'):
        num = ord('A')
    else:
        num += 1


    nx = x + dx[dir]
    ny = y + dy[dir]

    if (nx < 0 or nx >= n or ny < 0 or ny >= m) or grid[nx][ny] != 0:
        dir = (dir + 1) % 4
        x = x + dx[dir]
        y = y + dy[dir]
        continue

    x = nx
    y = ny

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()