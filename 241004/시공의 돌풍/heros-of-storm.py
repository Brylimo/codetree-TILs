n, m, t = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0] * m
    for _ in range(n)
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cleaner = []
# 시공의 돌풍 좌표 기록
for i in range(n):
    if grid[i][0] == -1:
        cleaner.append((i, 0))

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True

def spread():
    # 초기화
    for i in range(n):
        for j in range(m):
            next_grid[i][j] = grid[i][j]

    for i in range(n):
        for j in range(m):
            amount = grid[i][j]

            if amount == -1:
                continue

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if in_range(nx, ny) and grid[nx][ny] != -1:
                    next_grid[nx][ny] += (amount // 5)
                    next_grid[i][j] -= (amount // 5)

    # 최종 먼지값 옮기기
    for i in range(n):
        for j in range(m):
            grid[i][j] = next_grid[i][j]

def clean():
    # 초기화
    for i in range(n):
        for j in range(m):
            next_grid[i][j] = grid[i][j]

    up, down = cleaner[0], cleaner[1]

    next_grid[up_path[0][0]][up_path[0][1]] = 0
    # 위에 부분 청소
    for i in range(len(up_path) - 1):
        next_grid[up_path[i + 1][0]][up_path[i + 1][1]] = grid[up_path[i][0]][up_path[i][1]]


    next_grid[down_path[0][0]][down_path[0][1]] = 0
    # 위에 부분 청소
    for i in range(len(down_path) - 1):
        next_grid[down_path[i + 1][0]][down_path[i + 1][1]] = grid[down_path[i][0]][down_path[i][1]]

    # 최종 먼지값 옮기기
    for i in range(n):
        for j in range(m):
            grid[i][j] = next_grid[i][j]

up_path = []
down_path = []
def init():
    up, down = cleaner[0], cleaner[1]

    # 위에 부분 경로 기록
    dir = 1

    ux, uy = up[0], up[1]
    while True:
        nx = ux + dx[dir]
        ny = uy + dy[dir]

        if not in_range(nx, ny):
            dir = (dir + 3) % 4

            nx = ux + dx[dir]
            ny = uy + dy[dir]

        if nx == up[0] and ny == up[1]:
            break

        up_path.append((nx, ny))
        ux, uy = nx, ny

    # 아래 부분 경로 기록
    dir = 1

    wx, wy = down[0], down[1]
    while True:
        nx = wx + dx[dir]
        ny = wy + dy[dir]

        if not in_range(nx, ny):
            dir = (dir + 1) % 4

            nx = wx + dx[dir]
            ny = wy + dy[dir]

        if nx == down[0] and ny == down[1]:
            break

        down_path.append((nx, ny))
        wx, wy = nx, ny

init()
for _ in range(t):
    # 먼지 확산
    spread()

    # 청소
    clean()

ans = sum([
    grid[i][j]
    for i in range(n)
    for j in range(m)
    if grid[i][j] > -1
])
print(ans)