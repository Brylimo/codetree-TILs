n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0] * n
    for _ in range(n)
]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

path = []
def init():
    pdx = [0, 1, 0, -1]
    pdy = [-1, 0, 1, 0]

    x, y = n // 2, n // 2

    dir = 0
    dist = 1

    while x or y:
        for _ in range(dist):
            x = x + pdx[dir]
            y = y + pdy[dir]

            path.append((x, y))

            if not x and not y:
                break

        if dir == 1 or dir == 3:
            dist += 1

        dir = (dir + 1) % 4

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

def gravity():
    # 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0

    idx = 0
    for i in range(len(path)):
        xi, yi = path[i]

        if grid[xi][yi] > 0:
            next_grid[path[idx][0]][path[idx][1]] = grid[xi][yi]

            idx += 1

    # 중력이 발생한 뒤 결과물을 옮기기
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

ans = 0
def attack(d, p):
    global ans

    x, y = n // 2, n // 2

    for i in range(1, p + 1):
        nx = x + dx[d] * i
        ny = y + dy[d] * i

        if in_range(nx, ny):
            ans += grid[nx][ny]
            grid[nx][ny] = 0

    gravity()

flag = False
def get_next_idx(idx):
    global flag, ans

    tlst = []

    j = -1
    for i in range(idx, len(path) - 1):
        tlst.append((path[i][0], path[i][1]))

        if grid[path[i][0]][path[i][1]] != grid[path[i + 1][0]][path[i + 1][1]]:
            j = i + 1
            break

    if len(tlst) >= 4:
        for tx, ty in tlst:
            ans += grid[tx][ty]
            grid[tx][ty] = 0

        flag = True

    return j

def red_bomb():
    global flag

    flag = False

    i = 0
    while i < len(path):
        xi, yi = path[i]

        if grid[xi][yi] == 0:
            break

        i = get_next_idx(i)

        if i == -1:
            break

    gravity()

def calculate():
    # 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0

    tlst = []

    i = 0
    while i < len(path):
        xi, yi = path[i]

        if grid[xi][yi] == 0:
            break

        j = get_next_idx(i)
        tlst.append((j - i, grid[xi][yi]))

        i = j
        if i == -1:
            break

    for idx, (a, b) in enumerate(tlst):
        if idx * 2 >= len(path):
            break

        next_grid[path[idx * 2][0]][path[idx * 2][1]] = a
        next_grid[path[idx * 2 + 1][0]][path[idx * 2 + 1][1]] = b

    # 옮겨 담기
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

init()
for _ in range(m):
    d, p = map(int, input().split())

    # 몬스터 공격
    attack(d, p)

    # 중복된 몬스터 삭제
    red_bomb()

    while flag:
        red_bomb()

    calculate()

print(ans)