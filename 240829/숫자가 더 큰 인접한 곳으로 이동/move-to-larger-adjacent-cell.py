n, r, c = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def move(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    print(grid[x][y], end=" ")

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if grid[nx][ny] > grid[x][y]:
            move(nx, ny)
            break

move(r - 1, c - 1)