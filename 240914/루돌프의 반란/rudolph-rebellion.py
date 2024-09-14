import heapq

n, m, p, c, d = map(int, input().split())
rx, ry = map(int, input().split())
rx, ry = rx - 1, ry - 1

santas = dict()
scores = [0] * (p + 1)
rudolf_t = []

for _ in range(p):
    pn, sx, sy = map(int, input().split())
    santas[pn] = (sx - 1, sy - 1, 0)


def get_dist(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def santa_print():
    for i in range(1, p + 1):
        x, y, faint = santas[i]

        print(i, x, y, faint)

    print()

def sit_print():
    grid = [
        [0] * n
        for _ in range(n)
    ]

    for i in range(1, p + 1):
        x, y, faint = santas[i]

        grid[x][y] = i

    grid[rx][ry] = 'r'

    for i in range(n):
        print(grid[i])
def santa_calc(sx, sy):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    min_cost = int(1e9)
    dir = -1
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        tflag = False
        for j in range(1, p + 1):
            x, y, _ = santas[j]

            if nx == x and ny == y:
                tflag = True
                break

        if tflag:
            continue

        cost = get_dist(nx, ny, rx, ry)

        if cost < min_cost:
            min_cost = cost
            dir = i

    cost = get_dist(sx, sy, rx, ry)

    if min_cost >= cost:
        return -1

    return dir

def rudolf_calc(sx, sy):
    if ry == sy and rx > sx:
        return 0
    elif ry < sy and rx > sx:
        return 1
    elif ry < sy and rx == sx:
        return 2
    elif ry < sy and rx < sx:
        return 3
    elif ry == sy and rx < sx:
        return 4
    elif ry > sy and rx < sx:
        return 5
    elif ry > sy and rx == sx:
        return 6
    elif ry > sy and rx > sx:
        return 7

    return -1

def santa_crash(idx, x, y, flag, dir, option, pd):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    # 루돌프가 와 산타 충돌
    if option == 1:
        nx = x + dx[dir] * pd
        ny = y + dy[dir] * pd

        #print("ddstar", nx, ny)
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            santas[idx] = (-1, -1, 2)
            return

        for i in range(1, p + 1):
            ssx, ssy, ssflag = santas[i]

            if nx == ssx and ny == ssy:
                santa_crash(i, ssx, ssy, ssflag, dir, 0, 0)
                break

        santas[idx] = (nx, ny, 3)
    elif option == 2:
        nx = x + dx[dir] * pd
        ny = y + dy[dir] * pd

        #print("ddstar", nx, ny)
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            santas[idx] = (-1, -1, 2)
            return

        for i in range(1, p + 1):
            ssx, ssy, ssflag = santas[i]

            if nx == ssx and ny == ssy:
                santa_crash(i, ssx, ssy, ssflag, dir, 0, 0)
                break

        santas[idx] = (nx, ny, 2)
    else:  # 산타가 와 산타 충돌
        nx = x + dx[dir]
        ny = y + dy[dir]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            santas[idx] = (-1, -1, 0)
            return

        for i in range(1, p + 1):
            ssx, ssy, ssflag = santas[i]

            if nx == ssx and ny == ssy:
                santa_crash(i, ssx, ssy, ssflag, dir, 0, 0)

        # print("kill", nx, ny, flag)
        santas[idx] = (nx, ny, flag)

def rudolf_move(sx, sy):
    global rx, ry

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    dir = rudolf_calc(sx, sy)

    if dir == -1:
        return

    nx = rx + dx[dir]
    ny = ry + dy[dir]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        return

    for i in range(1, p + 1):
        ssx, ssy, ssflag = santas[i]

        # 이동하려는 좌표에 산타가 있으면
        if nx == ssx and ny == ssy:
            scores[i] += c
            santa_crash(i, ssx, ssy, ssflag, dir, 1, c)

    # 루돌프 이동
    rx, ry = nx, ny
    #print("rudolf", rx, ry)

def santa_move(idx, sx, sy, ssflag):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    dir = santa_calc(sx, sy)

    # 루돌프와 가까워질 수 없음
    if dir == -1:
        return

    nx = sx + dx[dir]
    ny = sy + dy[dir]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        return

    # 루돌프와 충돌
    if nx == rx and ny == ry:
        #print("ccrash")
        scores[idx] += d

        next_dir = 0
        if dir == 0:
            next_dir = 2
        elif dir == 1:
            next_dir = 3
        elif dir == 2:
            next_dir = 0
        elif dir == 3:
            next_dir = 1

        right_way = {
            0: 0,
            1: 2,
            2: 4,
            3: 6
        }

        santa_crash(idx, nx, ny, ssflag, right_way[next_dir], 2, d)
    else:
        if not (santas[idx][0] == -1 and santas[idx][1] == -1):
            santas[idx] = (nx, ny, 0)
    # santa_print()

for _ in range(m):
    # 루돌프가 산타 위치 확인
    for sidx in range(1, p + 1):
        sx, sy, flag = santas[sidx]

        if sx == -1 and sy == -1:
            continue

        distt = get_dist(sx, sy, rx, ry)

        heapq.heappush(rudolf_t, (distt, -sx, -sy, sidx))

    # 루돌프가 가야할 산타 정보
    _, fx, fy, fidx = heapq.heappop(rudolf_t)
    rudolf_t = []

    # 루돌프가 움직임
    rudolf_move(-fx, -fy)
    #santa_print()

    #sit_print()

    # 산타 차례
    for i in range(1, p + 1):
        x, y, flag = santas[i]

        if x == -1 and y == -1:
            continue

        if flag == 3:
            santas[i] = (x, y, 2)
            continue
        elif flag == 2:
            santas[i] = (x, y, 1)
            continue
        elif flag == 1:
            santas[i] = (x, y, 0)

        # 산타가 움직임
        santa_move(i, x, y, flag)

    out_cnt = 0
    for i in range(1, p + 1):
        if not (santas[i][0] == -1 and santas[i][1] == -1):
            scores[i] += 1
        else:
            out_cnt += 1

    if out_cnt == p:
        break

for i in range(1, p + 1):
    print(scores[i], end=" ")