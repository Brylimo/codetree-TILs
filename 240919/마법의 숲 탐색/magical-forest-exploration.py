from collections import deque

r, c, k = map(int, input().split())

grid = [
    [0] * (c + 1)
    for _ in range(r + 2)
]
visited = [
    [False] * (c + 1)
    for _ in range(r + 2)
]
doors = [
    [False] * (c + 1)
    for _ in range(r + 2)
]

golem = (-1, -1)
done = False
exits = [-1] * (k + 1)
ans = 0

dx = [0, -1, 0, 0, 1]
dy = [0, 0, 1, -1, 0]

mdx = [-1, 0, 1, 0]
mdy = [0, 1, 0, -1]

def show():
    for i in range(2, r + 2):
        print(grid[i][1:])
    print()

def show_visited():
    for i in range(2, r + 2):
        print(visited[i][1:])
    print()

def is_inrange(x, y):
    if 0 <= x <= r + 1 and 1 <= y <= c:
        return True

    return False

def put(idx):
    x, y = golem

    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]

        if is_inrange(nx, ny):
            grid[nx][ny] = idx

def is_okay(idx, cx, cy):
    flag = True
    for i in range(5):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if not (is_inrange(nx, ny) and (grid[nx][ny] == idx or grid[nx][ny] == 0)):
            flag = False
            break

    return flag

def golem_try(idx, bx, by, cx, cy):
    global golem, done

    # 기존 골렘 삭제
    for i in range(5):
        nx = bx + dx[i]
        ny = by + dy[i]

        grid[nx][ny] = 0

    for i in range(5):
        nx = cx + dx[i]
        ny = cy + dy[i]

        grid[nx][ny] = idx

    if cx == r:
        done = True

    golem = (cx, cy)

def golem_move(idx):
    global done

    while not done:
        # 남쪽으로 1칸 이동
        cx, cy = golem

        nx = cx + mdx[2]
        ny = cy + mdy[2]

        if is_okay(idx, nx, ny):
            golem_try(idx, cx, cy, nx, ny)
        else:
            # 서쪽으로 한칸 이동
            nx = cx + mdx[3]
            ny = cy + mdy[3]

            sx = nx + mdx[2]
            sy = ny + mdy[2]

            if is_okay(idx, nx, ny) and is_okay(idx, sx, sy):
                golem_try(idx, cx, cy, sx, sy)
                # 출구 이동
                exits[idx] = (exits[idx] + 3) % 4
            else:
                # 서쪽으로 한칸 이동
                nx = cx + mdx[1]
                ny = cy + mdy[1]

                sx = nx + mdx[2]
                sy = ny + mdy[2]

                if is_okay(idx, nx, ny) and is_okay(idx, sx, sy):
                    golem_try(idx, cx, cy, sx, sy)
                    # 출구 이동
                    exits[idx] = (exits[idx] + 1) % 4
                else:
                    done = True

    # 몸의 일부가 바깥에 있음
    if golem[0] <= 2:
        # grid 초기화
        for i in range(r + 2):
            for j in range(c + 1):
                grid[i][j] = 0
                doors[i][j] = False

        return True

    return False

def bfs(idx, x, y):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y, idx))

    while queue:
        ax, ay, id = queue.popleft()

        for i in range(4):
            nx = ax + mdx[i]
            ny = ay + mdy[i]

            if not is_inrange(nx, ny):
                continue

            if not visited[nx][ny] and (grid[nx][ny] == id or (doors[ax][ay] and grid[nx][ny] > 0)):
                visited[nx][ny] = True
                queue.append((nx, ny, grid[nx][ny]))

def elf_move(idx):
    global ans
    sx, sy = golem

    # 초기화
    for i in range(r + 2):
        for j in range(c + 1):
            visited[i][j] = False

    bfs(idx, sx, sy)

    # 가장 남쪽 행 구해서 더함
    for i in range(r + 1, -1, -1):
        for j in range(c + 1):
            if visited[i][j]:
                ans += i - 1
                return

query = []
for i in range(k):
    ci, di = map(int, input().split())
    query.append((ci, di))

for i in range(k):
    ci, di = query[i]
    idx = i + 1
    done = False
    exits[idx] = di

    # 골렘 도착
    golem = (1, ci)

    # 골렘 이동
    wiped = golem_move(idx)

    if wiped:
        continue

    # 골렘 문 표시
    kx = golem[0] + mdx[exits[idx]]
    ky = golem[1] + mdy[exits[idx]]

    doors[kx][ky] = True

    # 정령 움직임
    elf_move(idx)

print(ans)