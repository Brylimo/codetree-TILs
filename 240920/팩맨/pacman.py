from copy import deepcopy

n = 4
m, t = map(int, input().split())
r, c = map(int, input().split())
monsters = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

grid = [
    [[] for _ in range(n + 1)]
    for _ in range(n + 1)
]
next_grid = [
    [[] for _ in range(n + 1)]
    for _ in range(n + 1)
]
eggs = [
    [[] for _ in range(n + 1)]
    for _ in range(n + 1)
]
bodies = [
    [[0] * (n + 1)
    for _ in range(n + 1)]
    for _ in range(3)
]

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

def in_range(x, y):
    if 1 <= x <= 4 and 1 <= y <= 4:
        return True
    return False

def duplicate():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 몬스터가 존재
            if len(grid[i][j]) > 0:
                for m in grid[i][j]:
                    dir = m
                    eggs[i][j].append(dir)

def monster_move():
    global grid, next_grid

    next_grid = deepcopy(grid)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if len(grid[i][j]) <= 0:
                continue

            for idx, m in enumerate(grid[i][j]):
                dir = m

                while True:
                    nx = i + dx[dir]
                    ny = j + dy[dir]

                    if not in_range(nx, ny) or bodies[2][nx][ny] > 0 or bodies[1][nx][ny] > 0 or bodies[0][nx][ny] > 0 or (nx == r and ny == c):
                        # 반시계 회전
                        dir = (dir % 8) + 1

                        # 현재 방향
                        if dir == m:
                            break
                    else:
                        for k in range(len(next_grid[i][j])):
                            if next_grid[i][j][k] == m:
                                next_grid[i][j].pop(k)
                                break
                        next_grid[nx][ny].append(dir)
                        break

    grid = deepcopy(next_grid)

max_val = 0
max_candidate = []
candidate = []
def calculate(idx, score):
    global max_val, max_candidate

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    # 종료조건
    if idx == 3:
        if max_val < score:
            max_val = score
            max_candidate = deepcopy(candidate)
        return

    x, y = candidate[-1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not in_range(nx, ny):
            continue

        flag = False
        if (nx, ny) in candidate:
            flag = True

        candidate.append((nx, ny))
        if flag:
            calculate(idx + 1, score)
        else:
            calculate(idx + 1, score + len(grid[nx][ny]))
        candidate.pop()

def packman_move():
    global max_candidate, candidate, max_val, r, c

    candidate.append((r, c))
    calculate(0, 0)

    for x, y in max_candidate[1:]:
        if len(grid[x][y]) > 0:
            bodies[2][x][y] = len(grid[x][y])
            grid[x][y] = []

    r, c = max_candidate[-1]

    max_candidate = []
    candidate = []
    max_val = 0

def body_diappear():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            bodies[0][i][j] = bodies[1][i][j]
            bodies[1][i][j] = bodies[2][i][j]
            bodies[2][i][j] = 0

def hatch():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if len(eggs[i][j]) > 0:
                while eggs[i][j]:
                    d = eggs[i][j].pop()
                    grid[i][j].append(d)

# 몬스터 초기화
for i in range(m):
    x, y, d = monsters[i]
    grid[x][y].append(d)

for _ in range(t):
    # 몬스터 복제 시도
    duplicate()

    # 몬스터 이동
    monster_move()

    # 팩맨 이동
    packman_move()

    # 몬스터 시체 관리
    body_diappear()

    # 몬스터 알 부화
    hatch()

ans = sum([
    len(grid[i][j])
    for i in range(1, n + 1)
    for j in range(1, n + 1)
])

print(ans)