n = int(input())
x, y = map(int, input().split())
grid = [
    list(input())
    for _ in range(n)
]
visited = [
    [[False] * 4 for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    return True

def move(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    dir = 0

    visited[x][y][dir] = True
    tick = 0
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]

        if in_range(nx, ny):
            if grid[nx][ny] != '#' and not visited[nx][ny][dir]:
                if in_range(nx + 1, ny) and grid[nx + 1][ny] == '#':
                    x, y = nx, ny
                    visited[x][y][dir] = True
                else:
                    x, y = nx, ny
                    visited[x][y][dir] = True
                    dir = (dir + 1) % 4
                    visited[x][y][dir] = True
                tick += 1
            elif visited[nx][ny][dir]:
                return -1
            else:
                dir = (dir + 3) % 4
                if visited[x][y][dir]:
                    return -1
                visited[x][y][dir] = True
        else:
            tick += 1
            break

    return tick

ans = move(x - 1, y - 1)
print(ans)