import sys
from collections import deque
INT_MAX = sys.maxsize

n, m, p, c, d = map(int, input().split())
rr, rc = map(int, input().split())
rr, rc = rr - 1, rc - 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

santa_score = [0] * (p + 1)
santa_x = [0] * (p + 1)
santa_y = [0] * (p + 1)
outs = [False] * (p + 1)
faints = [0] * (p + 1)
grid = [
    [0] * n
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]
steps = [
    [0] * n
    for _ in range(n)
]

for _ in range(p):
    sn, sr, sc = map(int, input().split())

    santa_x[sn] = sr - 1
    santa_y[sn] = sc - 1

    grid[sr - 1][sc - 1] = sn

def get_dist(r1, c1, r2, c2):
    return (r1 - r2) ** 2 + (c1 - c2) ** 2

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    return True

def rudolf_move(k):
    global rr, rc

    temp_list = []
    for i in range(1, p + 1):
        if outs[i]:
            continue

        sr, sc = santa_x[i], santa_y[i]

        distance = get_dist(sr, sc, rr, rc)
        temp_list.append((distance, -sr, -sc))

    temp_list.sort()

    # 가장 가까운 산타 정보
    if len(temp_list) <= 0:
        return

    dist, sr, sc = temp_list[0]
    sr, sc = -sr, -sc

    dx, dy = -1, -1
    if rr < sr:
        dx = 1
    elif rr == sr:
        dx = 0
    elif rr > sr:
        dx = -1

    if rc < sc:
        dy = 1
    elif rc == sc:
        dy = 0
    elif rc > sc:
        dy = -1

    nx = rr + dx
    ny = rc + dy

    if in_range(nx, ny):
        rr, rc = nx, ny

        # 산타와 충돌
        if grid[nx][ny] > 0:
            idx = grid[nx][ny]

            santa_score[idx] += c
            faints[idx] = k + 1

            # 산타 밀려남
            snx = nx + dx * c
            sny = ny + dy * c

            if not in_range(snx, sny):
                outs[idx] = True
                grid[nx][ny] = 0
            else:
                if grid[snx][sny] > 0:
                    # 상호작용
                    chain_reaction(snx, sny, dx, dy)

                grid[nx][ny] = 0
                grid[snx][sny] = idx
                santa_x[idx] = snx
                santa_y[idx] = sny

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    steps[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not in_range(nx, ny):
                continue

            if not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                steps[nx][ny] = steps[x][y] + 1
                queue.append((nx, ny))

def santa_move(k):
    for i in range(1, p + 1):
        if outs[i] or faints[i] > 0:
            continue

        sx, sy = santa_x[i], santa_y[i]

        org_dist = get_dist(rr, rc, sx, sy)

        dir = -1
        min_x, min_y = -1, -1
        min_dist = org_dist
        for j in range(4):
            nx = sx + dx[j]
            ny = sy + dy[j]

            if not in_range(nx, ny) or grid[nx][ny] > 0:
                continue

            temp_dist = get_dist(rr, rc, nx, ny)
            if temp_dist < min_dist:
                min_dist = temp_dist
                min_x, min_y = nx, ny
                dir = j

        if min_x == -1 and min_y == -1:
            continue

        # 루돌프와 충돌
        if min_x == rr and min_y == rc:
            santa_score[i] += d
            faints[i] = k + 1
            dir = (dir + 2) % 4

            snx = min_x + dx[dir] * d
            sny = min_y + dy[dir] * d

            if not in_range(snx, sny):
                outs[i] = True
                grid[sx][sy] = 0
                continue

            # 상호작용
            if grid[snx][sny] > 0 and grid[snx][sny] != i:
                chain_reaction(snx, sny, dx[dir], dy[dir])
                grid[snx][sny] = i
                grid[sx][sy] = 0
                santa_x[i] = snx
                santa_y[i] = sny

                continue
            else:
                grid[snx][sny] = i
                grid[sx][sy] = 0
                santa_x[i] = snx
                santa_y[i] = sny

                continue

        grid[sx][sy] = 0
        grid[min_x][min_y] = i
        santa_x[i] = min_x
        santa_y[i] = min_y

def chain_reaction(x, y, ddx, ddy):
    current_idx = grid[x][y]

    nx = x + ddx
    ny = y + ddy

    if not in_range(nx, ny):
        outs[current_idx] = True
        return

    # 산타를 만남
    if grid[nx][ny] > 0:
        print("hi")
        chain_reaction(nx, ny, ddx, ddy)

    grid[nx][ny] = current_idx
    santa_x[current_idx] = nx
    santa_y[current_idx] = ny

for k in range(1, m + 1):
    # 루돌프 움직임
    rudolf_move(k)

    # 산타 움직임
    santa_move(k)

    for i in range(1, p + 1):
        if outs[i]:
            continue

        santa_score[i] += 1
        if faints[i] == k:
            faints[i] = 0

    if all(outs):
        break

for i in range(1, p + 1):
    print(santa_score[i], end=" ")