EMPTY = (-1, -1)

n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0] * n
    for _ in range(n)
]
deal = [
    [EMPTY] * n
    for _ in range(n)
]
dirs = [0] + list(map(int, input().split()))
prio = [
    [
        [0] * 4
        for _ in range(4)
    ]
    for _ in range(m + 1)
]

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

alive = [True] * (m + 1)
elapsed_time = 0
for i in range(m * 4):
    prio[(i // 4) + 1][i % 4][:] = map(int, input().split())

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    return True

def init():
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                deal[i][j] = (k, grid[i][j])

def end():
    if elapsed_time >= 1000:
        return True

    alive_cnt = 0
    for i in range(1, m + 1):
        if alive[i]:
            alive_cnt += 1

    if alive_cnt == 1 and alive[1]:
        return True

    return False

def move_all():
    # 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[i][j]

    next_deal = [arr[:] for arr in deal]

    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0 and alive[grid[i][j]]:
                # 플레이어 번호
                num = grid[i][j]
                dirr = dirs[num]

                directions = prio[num][dirr - 1]

                fx, fy = -1, -1
                for dir in directions:
                    nx = i + dx[dir]
                    ny = j + dy[dir]

                    if not in_range(nx, ny):
                        continue

                    # 아무도 독점 계약 하지 않음
                    if deal[nx][ny] == EMPTY:
                        fx, fy = nx, ny
                        dirs[num] = dir
                        break

                # 아무도 독점 계약 하지 않은 칸이 없음
                if fx == -1 and fy == -1:
                    for dir in directions:
                        nx = i + dx[dir]
                        ny = j + dy[dir]

                        if not in_range(nx, ny):
                            continue

                        if deal[nx][ny] != EMPTY and deal[nx][ny][1] == num:
                            fx, fy = nx, ny
                            dirs[num] = dir
                            break

                next_grid[i][j] = 0
                # 이동하려는 칸에 사람이 존재함
                if next_grid[fx][fy] != num and next_grid[fx][fy] > 0:
                    if next_grid[fx][fy] > num:
                        alive[next_grid[fx][fy]] = False
                        next_grid[fx][fy] = num
                        next_deal[fx][fy] = (k + 1, num)
                    else:
                        alive[num] = False
                else: # 사람이 존재하지 않음
                    next_grid[fx][fy] = num
                    next_deal[fx][fy] = (k + 1, num)

    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]
            deal[i][j] = next_deal[i][j]

def subtract():
    for i in range(n):
        for j in range(n):
            if deal[i][j] != EMPTY:
                d_cnt, num = deal[i][j]
                if d_cnt - 1 == 0:
                    deal[i][j] = EMPTY
                else:
                    deal[i][j] = (d_cnt - 1, num)

init()
while not end():
    # 플레이어 이동
    move_all()

    # 계약 1 줄임
    subtract()

    elapsed_time += 1


if elapsed_time >= 1000:
    print(-1)
else:
    print(elapsed_time)