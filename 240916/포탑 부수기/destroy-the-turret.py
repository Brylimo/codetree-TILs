import heapq
from collections import deque

n, m, k = map(int, input().split())
grid = [
    [0] * (n + 1)
    for _ in range(m + 1)
]
visited = [
    [False] * (n + 1)
    for _ in range(m + 1)
]
tracker = [
    [None] * (n + 1)
    for _ in range(m + 1)
]
turns = [
    [0] * (n + 1)
    for _ in range(m + 1)
]
injured = [
    [False] * (n + 1)
    for _ in range(m + 1)
]
weaks = []
strongs = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

attacker = (-1, -1, -1, -1, -1, -1)
victim = (-1, -1, -1, -1, -1, -1)
plus_energy = n + m

def show():
    for i in range(1, n + 1):
        print(grid[i][1:])
    print()

def show_tracker():
    for i in range(1, n + 1):
        print(tracker[i][1:])
    print()

def is_inrange(x, y):
    if 1 <= x <= n and 1 <= y <= m:
        return True

    return False

def select_attacker():
    global attacker, weaks

    # 가장 약한 포탑을 선별
    if weaks:
        attacker = heapq.heappop(weaks)
        weaks = []

def select_victim():
    global victim, strongs

    # 가장 강한 포탑을 선별
    if strongs:
        victim = heapq.heappop(strongs)
        strongs = []


def laser_tracking():
    global attacker

    if not (attacker and victim):
        return

    s_energy, _, _, _, sx, sy = attacker
    _, _, _, _, ex, ey = victim

    damage = (s_energy + plus_energy) // 2
    x, y = ex, ey

    while tracker[x][y]:
        bx, by = tracker[x][y]
        x, y = bx, by

        if x == sx and y == sy:
            break

        injured[x][y] = True
        after_energy = grid[x][y] - damage
        if after_energy > 0:
            grid[x][y] = after_energy
        else:
            grid[x][y] = 0

def laser_attack():
    # 초기화
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            visited[i][j] = False
            tracker[i][j] = None

    queue = deque()
    if attacker and victim:
        s_energy, _, _, _, sx, sy = attacker
        _, _, _, _, ex, ey = victim

        queue.append((sx, sy))
        visited[sx][sy] = True

        injured[sx][sy] = True
        injured[ex][ey] = True

        while queue:
            x, y = queue.popleft()

            if x == ex and y == ey:
                break

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not is_inrange(nx, ny):
                    # 상
                    if i == 3:
                        nx = n
                    # 하
                    elif i == 1:
                        nx = 1
                    # 좌
                    elif i == 2:
                        ny = m
                    # 우
                    elif i == 0:
                        ny = 1

                # 벽
                if grid[nx][ny] == 0:
                    continue

                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    tracker[nx][ny] = (x, y)
                    queue.append((nx, ny))

        # 피해자를 방문함
        if visited[ex][ey]:
            # 피해자 피해 반영
            after_energy = grid[ex][ey] - (s_energy + plus_energy)
            if after_energy > 0:
                grid[ex][ey] = after_energy
            else:
                grid[ex][ey] = 0

            # 공격 받은 포탑 피해 반영
            laser_tracking()
            return True
        else:
            return False

    else:
        return False


def bomb_attack():
    bx = [-1, -1, 0, 1, 1, 1, 0, -1]
    by = [0, 1, 1, 1, 0, -1, -1, -1]

    if attacker and victim:
        s_energy, _, _, _, sx, sy = attacker
        _, _, _, _, ex, ey = victim

        injured[sx][sy] = True
        injured[ex][ey] = True

        # 피해자가 데미지를 입음
        after_energy = grid[ex][ey] - (s_energy + plus_energy)
        if after_energy > 0:
            grid[ex][ey] = after_energy
        else:
            grid[ex][ey] = 0

        # 8 방향에서 데미지를 입음
        for i in range(8):
            nx = ex + bx[i]
            ny = ey + by[i]

            if not is_inrange(nx, ny):
                # 0
                if i == 0:
                    nx = n
                # 1
                elif i == 1:
                    if not (1 <= nx <= n):
                        nx = n
                    if not (1 <= ny <= m):
                        ny = 1
                # 2
                elif i == 2:
                    ny = 1
                # 3
                elif i == 3:
                    if not (1 <= nx <= n):
                        nx = 1
                    if not (1 <= ny <= m):
                        ny = 1
                # 4
                if i == 4:
                    nx = 1
                # 5
                elif i == 5:
                    if not (1 <= nx <= n):
                        nx = 1
                    if not (1 <= ny <= m):
                        ny = m
                # 6
                if i == 6:
                    ny = m
                # 7
                if i == 7:
                    if not (1 <= nx <= n):
                        nx = n
                    if not (1 <= ny <= m):
                        ny = m

            if injured[nx][ny]:
                continue

            if grid[nx][ny] > 0:
                injured[nx][ny] = True

                aftermath = grid[nx][ny] - ((s_energy + plus_energy) // 2)
                if aftermath > 0:
                    grid[nx][ny] = aftermath
                else:
                    grid[nx][ny] = 0

def attack():
    # laser
    if not laser_attack():
        # bomb
        bomb_attack()


def maintenance():
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if grid[i][j] > 0 and not injured[i][j]:
                grid[i][j] += 1

            injured[i][j] = False

for i in range(1, n + 1):
    grid[i][1:] = map(int, input().split())

for turn in range(1, k + 1):
    alive_cnt = 0

    # heap 초기화
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            energy = grid[i][j]

            # 에너지가 0이면 제외
            if energy <= 0:
                continue

            heapq.heappush(weaks, (energy, -turns[i][j], -(i + j), -j, i, j))
            heapq.heappush(strongs, (-energy, turns[i][j], (i + j), j, i, j))

            alive_cnt += 1

    if alive_cnt == 1:
        break

    # 공격자 선정
    select_attacker()

    # 피해자 선정
    select_victim()

    # 공격자 공격
    attack()

    s_energy, _, _, _, sx, sy = attacker
    turns[sx][sy] = turn
    grid[sx][sy] = s_energy + plus_energy

    # 포탑 정비
    maintenance()

ans = max([
    grid[i][j]
    for i in range(1, n + 1)
    for j in range(1, m + 1)
])
print(ans)