n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
coldness = [
    [0] * n
    for _ in range(n)
]
next_coldness = [
    [0] * n
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]
wall = [
            [[] for _ in range(n)]
            for _ in range(n)
]

ac = []

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for _ in range(m):
    x, y, s = map(int, input().split())
    wall[x - 1][y - 1].append(s)

# 에어컨 위치 기록
for i in range(n):
    for j in range(n):
        if grid[i][j] > 1:
            ac.append((i, j, grid[i][j]))

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    return True

def canGo(sx, sy, ox, oy, dir):
    if not in_range(ox, oy):
        return False

    if (dir == 1 and 0 in wall[sx][sy]) or (dir == 2 and 1 in wall[sx][sy]):
        return False

    if (dir == 3 and 0 in wall[ox][oy]) or (dir == 2 and 1 in wall[ox][oy]):
        return False

    return True

def wind_move(sx, sy, dir, st):
    cw = (dir + 1) % 4
    ccw = (dir + 3) % 4

    if st == 0:
        return

    left, straight, right = False, False, False

    ox1 = sx + dx[ccw]
    oy1 = sy + dy[ccw]

    ox2 = ox1 + dx[dir]
    oy2 = oy1 + dy[dir]

    if canGo(sx, sy, ox1, oy1, ccw) and canGo(ox1, ox2, ox2, oy2, dir) and not visited[ox2][oy2]:
        coldness[ox2][oy2] += st
    else:
        left = True

    nx = sx + dx[dir]
    ny = sy + dy[dir]

    if canGo(sx, sy, nx, ny, dir) and not visited[nx][ny]:
        coldness[nx][ny] += st
    else:
        straight = True

    tx1 = sx + dx[cw]
    ty1 = sy + dy[cw]

    tx2 = tx1 + dx[dir]
    ty2 = ty1 + dy[dir]

    if canGo(sx, sy, tx1, ty1, cw) and canGo(tx1, ty1, tx2, ty2, dir) and not visited[tx2][ty2]:
        coldness[tx2][ty2] += st
    else:
        right = True

    if not left:
        visited[ox2][oy2] = True
        wind_move(ox2, oy2, dir, st - 1)
    if not straight:
        visited[nx][ny] = True
        wind_move(nx, ny, dir, st - 1)
    if not right:
        visited[tx2][ty2] = True
        wind_move(tx2, ty2, dir, st - 1)

def wind():
    for i, j, dir in ac:
        dir -= 2

        nx = i + dx[dir]
        ny = j + dy[dir]

        if in_range(nx, ny):
            for i in range(n):
                for j in range(n):
                    visited[i][j] = False

            coldness[nx][ny] += 5
            visited[nx][ny] = True
            # 바람 이동
            wind_move(nx, ny, dir, 4)

def combi():
    for i in range(n):
        for j in range(n):
            next_coldness[i][j] = coldness[i][j]

    for i in range(n):
        for j in range(n):

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if in_range(nx, ny) and canGo(i, j, nx, ny, k) and coldness[i][j] > coldness[nx][ny]:
                    diff = abs(coldness[i][j] - coldness[nx][ny]) // 4

                    next_coldness[i][j] -= diff
                    next_coldness[nx][ny] += diff

    for i in range(n):
        for j in range(n):
            coldness[i][j] = next_coldness[i][j]

def side_effect():
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                coldness[i][j] -= 1

                if coldness[i][j] < 0:
                    coldness[i][j] = 0

time = 0
while True:
    if time > 100:
        time = -1
        break

    # 에어컨 바람
    wind()

    # 시원한 공기 섞임
    combi()

    # 외벽 감소
    side_effect()

    time += 1

    flag = True
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and coldness[i][j] < k:
                flag = False
                break
        if not flag:
            break

    if flag:
        break

print(time)