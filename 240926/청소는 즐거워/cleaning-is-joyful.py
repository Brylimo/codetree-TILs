import math

n = int(input())
grid = [
    [-1] * (n + 8)
    for _ in range(n + 8)
]
visited = [
    [False] * (n + 8)
    for _ in range(n + 8)
]

spiral = []

for i in range(4, n + 4):
    grid[i][4:n+4] = map(int, input().split())

def in_range(x, y):
    if x < 4 or x >= n + 4 or y < 4 or y >= n + 4:
        return False
    return True

def init():
    x, y = n // 2 + 4, n // 2 + 4
    spiral.append((x, y, 0))

    visited[x][y] = True
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    dir = 0
    size = 1
    while not (x == 4 and y == 4):
        for i in range(size):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if in_range(nx, ny):
                spiral.append((nx, ny, dir))
                x, y = nx, ny

        dir = (dir + 1) % 4
        if dir == 0 or dir == 2:
            size += 1

ans = 0

def rotate(temp, next_temp, dir):
    if dir == 0:
        return

    for k in range(dir):
        for i in range(5):
            for j in range(5):
                next_temp[5 - j - 1][i] = temp[i][j]

        for i in range(5):
            for j in range(5):
                temp[i][j] = next_temp[i][j]

def clean(x, y, dir):
    global ans

    temp = [
        [0, 0, 2, 0, 0],
        [0, 10, 7, 1, 0],
        [5, -1, 0, 0, 0],
        [0, 10, 7, 1, 0],
        [0, 0, 2, 0, 0]
    ]

    next_temp = [
        [0] * 5
        for _ in range(5)
    ]

    rotate(temp, next_temp, dir)

    a_i, a_j = -1, -1
    current = grid[x][y]
    for i in range(x - 2, x + 3):
        for j in range(y - 2, y + 3):
            if temp[i - (x - 2)][j - (y - 2)] == -1:
                a_i, a_j = i, j
                continue

            if temp[i - (x - 2)][j - (y - 2)] > 0:
                value = math.floor(current * (temp[i - (x - 2)][j - (y - 2)] / 100))

                if grid[i][j] == -1:
                    ans += value
                else:
                    if visited[i][j]:
                        grid[x][y] -= value
                        continue

                    grid[i][j] += value

                grid[x][y] -= value

    visited[x][y] = True
    # a에 대한 처리
    if a_i != -1 and a_j != -1:
        value = grid[x][y]
        if grid[a_i][a_j] == -1:
            ans += value
        else:
            if visited[a_i][a_j]:
                visited[x][y] = True
                grid[x][y] = 0
                return

            grid[a_i][a_j] += value

        grid[x][y] = 0

init()
for x, y, d in spiral[1:]:
    clean(x, y, d)

print(ans)