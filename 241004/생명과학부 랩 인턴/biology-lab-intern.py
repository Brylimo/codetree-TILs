from copy import deepcopy

EMPTY = (-1, -1)
n, m, k = map(int, input().split())

grid = [
    [[] for _ in range(m)]
    for _ in range(n)
]
v = [0] * (k + 1)
dirs = [0] * (k + 1)
sizes = [0] * (k + 1)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

entity = [EMPTY] * (k + 1)
alive = [True] * (k + 1)
for idx in range(1, k + 1):
    x, y, s, d, b = map(int, input().split())
    grid[x - 1][y - 1].append(idx)

    v[idx] = s
    dirs[idx] = d - 1
    sizes[idx] = b
    entity[idx] = (x - 1, y - 1)

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True

def move_all():
    global grid

    next_grid = deepcopy(grid)

    for i in range(1, k + 1):
        if not alive[i]:
            continue

        x, y = entity[i]

        ax, ay = x, y
        for j in range(v[i]):
            nx = ax + dx[dirs[i]]
            ny = ay + dy[dirs[i]]

            if not in_range(nx, ny):
                if dirs[i] == 0:
                    dirs[i] = 1
                elif dirs[i] == 1:
                    dirs[i] = 0
                elif dirs[i] == 2:
                    dirs[i] = 3
                elif dirs[i] == 3:
                    dirs[i] = 2

                nx = ax + dx[dirs[i]]
                ny = ay + dy[dirs[i]]

            ax, ay = nx, ny

        next_grid[x][y].remove(i)
        next_grid[ax][ay].append(i)

        entity[i] = (ax, ay)

    grid = deepcopy(next_grid)
def eat():
    for i in range(n):
        for j in range(m):
            if len(grid[i][j]) > 1:
                max_idx = -1
                max_size = 0
                for k in grid[i][j]:
                    if sizes[k] > max_size:
                        max_size = sizes[k]
                        max_idx = k
                    alive[k] = False

                alive[max_idx] = True
                grid[i][j] = [max_idx]

ans = 0
for j in range(m):
    # 한 열을 모두 찾아봄
    for i in range(n):

        # 곰팡이 채취
        if len(grid[i][j]) > 0:
            idx = grid[i][j][0]

            ans += sizes[idx]
            grid[i][j] = []
            alive[idx] = False
            break

    # 곰팡이 이동
    move_all()

    # 잡아먹음
    eat()

print(ans)