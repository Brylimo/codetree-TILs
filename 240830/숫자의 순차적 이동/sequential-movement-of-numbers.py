n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def move(x, y):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    max_val = 0
    max_pos = (-1, -1)
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if grid[nx][ny] > max_val:
            max_val = grid[nx][ny]
            max_pos = (nx, ny)

    grid[x][y], grid[max_pos[0]][max_pos[1]] = grid[max_pos[0]][max_pos[1]], grid[x][y]
        

def move_all():
    for num in range(1, n * n + 1):
        flag = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == num:
                    move(i, j)
                    flag = True
                    break
            if flag:
                break

for _ in range(m):
    move_all()

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()