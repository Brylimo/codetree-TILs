n = 4
cn = 6
k = int(input())

blue_grid = [
    [0] * n
    for _ in range(n)
]
next_blue_grid = [
    [0] * n
    for _ in range(n)
]

red_grid = [
    [0] * n
    for _ in range(n + 2)
]

yellow_grid = [
    [0] * n
    for _ in range(n + 2)
]

blocks = [
    [[1]],
    [[1, 1]],
    [[1], [1]]
]

point = 0
def init():
    # 파란색 칸들 초기화
    for i in range(n):
        for j in range(n):
            blue_grid[i][j] = 0

def put(t, x, y):
    block = blocks[t - 1]

    for i in range(len(block)):
        for j in range(len(block[-1])):
            blue_grid[x + i][y + j] = 1

def yellow_fall():
    candidate = set()
    for i in range(n):
        for j in range(n):
            if blue_grid[i][j] == 1:
                candidate.add(j)

    idx = cn - 1
    for j in candidate:
        for i in range(cn - 1, -1, -1):
            if yellow_grid[i][j] == 1:
                idx = min(idx, i - 1)

    for j in range(n):
        kidx = idx
        for i in range(n - 1, -1, -1):
            if blue_grid[i][j] == 1:
                yellow_grid[kidx][j] = blue_grid[i][j]
                kidx -= 1

def red_fall():
    candidate = set()
    for i in range(n):
        for j in range(n):
            if blue_grid[i][j] == 1:
                candidate.add(j)

    idx = cn - 1
    for j in candidate:
        for i in range(cn - 1, -1, -1):
            if red_grid[i][j] == 1:
                idx = min(idx, i - 1)

    for j in range(n):
        kidx = idx
        for i in range(n - 1, -1, -1):
            if blue_grid[i][j] == 1:
                red_grid[kidx][j] = blue_grid[i][j]
                kidx -= 1

def rotate_blue():
    # 초기화
    for i in range(n):
        for j in range(n):
            next_blue_grid[i][j] = 0

    for i in range(n):
        for j in range(n):
            next_blue_grid[j][n - i - 1] = blue_grid[i][j]

    for i in range(n):
        for j in range(n):
            blue_grid[i][j] = next_blue_grid[i][j]

def inspect_grid(t_grid):
    global point

    for i in range(cn):
        flag = True
        for j in range(n):
            if t_grid[i][j] == 0:
                flag = False
                break

        if flag:
            point += 1
            del t_grid[i]
            t_grid = [[0] * n] + t_grid

    return t_grid

def inspect_grid2(t_grid):
    global point

    cnt = 0
    for j in range(n):
        if t_grid[0][j] == 1:
            cnt += 1
            break

    for j in range(n):
        if t_grid[1][j] == 1:
            cnt += 1
            break

    if cnt > 0:
        for i in range(cnt):
            del t_grid[-1]
            t_grid = [[0] * n] + t_grid

    return t_grid

for _ in range(k):
    t, x, y = map(int, input().split())

    init()

    # 블록을 파란색 칸에 집어넣음
    put(t, x, y)

    # 노란색 떨어짐
    yellow_fall()

    # 검사
    yellow_grid = inspect_grid(yellow_grid)

    # 연한 칸 검사
    yellow_grid = inspect_grid2(yellow_grid)

    # 파란색 회전
    rotate_blue()

    # 빨간색 떨어짐
    red_fall()

    # 검사
    red_grid = inspect_grid(red_grid)

    # 연한 칸 검사
    red_grid = inspect_grid2(red_grid)

print(point)

cnt = 0
for i in range(cn):
    for j in range(n):
        if red_grid[i][j] == 1:
            cnt += 1

        if yellow_grid[i][j] == 1:
            cnt += 1

print(cnt)