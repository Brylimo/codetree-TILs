n, m, h, k = map(int, input().split())

grid = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
tmap = [
    [[] for _ in range(n + 1)]
    for _ in range(n + 1)
]
visited = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

thief_x = [0] * (m + 1)
thief_y = [0] * (m + 1)
thief_type = [0] * (m + 1)
thief_dir = [0] * (m + 1)
thief_out = [False] * (m + 1)
chaser = (n // 2 + 1, n // 2 + 1, 0)
wheel = 1
vcnt = 0

points = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def show():
    for i in range(1, n + 1):
        print(visited[i][1:])
    print()

def show_tmap():
    for i in range(1, n + 1):
        print(tmap[i][1:])
    print()

def is_inrange(x, y):
    if 1 <= x <= n and 1 <= y <= n:
        return True

    return False


def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def thief_move():
    cx, cy, cdir = chaser

    # 전체 도망자 확인
    for i in range(1, m + 1):
        if thief_out[i]:
            continue

        x, y, type, dir = thief_x[i], thief_y[i], thief_type[i], thief_dir[i]

        # 술레와의 거리 확인
        dist = get_distance(cx, cy, x, y)

        if dist > 3:
            tmap[x][y].append(i)
            continue

        nx = x + dx[dir]
        ny = y + dy[dir]

        # 격자 out
        if not is_inrange(nx, ny):
            # 반대 방향으로 바꾸기
            dir = (dir + 2) % 4

            nx = x + dx[dir]
            ny = y + dy[dir]

            # 술레가 아니면 전진
            if not (nx == cx and ny == cy):
                thief_x[i] = nx
                thief_y[i] = ny
            else:
                tmap[x][y].append(i)
                thief_dir[i] = dir
                continue

            thief_dir[i] = dir
        else:
            # 술레가 있음
            if (nx == cx and ny == cy):
                tmap[x][y].append(i)
                continue

            thief_x[i] = nx
            thief_y[i] = ny

        tmap[nx][ny].append(i)


def chaser_move():
    global chaser, wheel, vcnt

    cx, cy, cdir = chaser
    next_dir = (cdir + wheel + 4) % 4

    if wheel == 1:
        # 술레 이동
        nx = cx + dx[cdir]
        ny = cy + dy[cdir]

        px = nx + dx[next_dir]
        py = ny + dy[next_dir]

        # 방향 바꿀 수 있으면 방향 바꿈
        if not visited[px][py]:
            cdir = next_dir

        # 술레 좌표 갱신
        chaser = (nx, ny, cdir)
        visited[nx][ny] = visited[cx][cy] + 1
        vcnt += 1
    else:
        #print("queen", cx, cy, cdir)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if is_inrange(nx, ny) and visited[nx][ny] == visited[cx][cy] - 1:
                visited[cx][cy] = 0
                chaser = (nx, ny, i)
                vcnt += 1

                px = nx + dx[i]
                py = ny + dy[i]

                if not is_inrange(px, py) or visited[px][py] != visited[nx][ny] - 1:
                    chaser = (nx, ny, (i + 3) % 4)
                break

    # 달팽이 다 돌음
    if vcnt == n * n:
        wheel *= -1

        # 방향은 반대
        cdir = (cdir + 2) % 4
        vcnt = 1

        chaser = (nx, ny, cdir)

def catch():
    cx, cy, cdir = chaser

    cnt = 0
    for i in range(3):
        nx = cx + dx[cdir] * i
        ny = cy + dy[cdir] * i

        if is_inrange(nx, ny) and grid[nx][ny] == 0:
            cnt += len(tmap[nx][ny])

            for j in range(len(tmap[nx][ny])):
                idx = tmap[nx][ny][j]
                thief_out[idx] = True

    return cnt

for i in range(1, m + 1):
    x, y, d = map(int, input().split())
    thief_x[i] = x
    thief_y[i] = y
    thief_type[i] = d

    if d == 1:
        thief_dir[i] = 1
    elif d == 2:
        thief_dir[i] = 2

visited[chaser[0]][chaser[1]] = 1
vcnt += 1

for i in range(h):
    x, y = map(int, input().split())
    grid[x][y] = 1

for turn in range(1, k + 1):
    # 도망자 이동
    thief_move()

    # 술레 이동
    chaser_move()

    # 술레 잡기
    catch_cnt = catch()

    # 정산
    points += turn * catch_cnt

    #show_tmap()

    # 초기화
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            tmap[i][j] = []

    #show()

print(points)