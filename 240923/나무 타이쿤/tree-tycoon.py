n, m = map(int, input().split())

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
special = [
    [False] * n
    for _ in range(n)
]
next_special = [
    [False] * n
    for _ in range(n)
]

special[n - 2][0] = True
special[n - 2][1] = True
special[n - 1][0] = True
special[n - 1][1] = True


def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    return True


def move(dir, p):
    for i in range(n):
        for j in range(n):
            next_special[i][j] = False

    for i in range(n):
        for j in range(n):
            if special[i][j]:
                nx = (i + dx[dir] * p) % n
                ny = (j + dy[dir] * p) % n

                next_special[nx][ny] = True

    for i in range(n):
        for j in range(n):
            special[i][j] = next_special[i][j]


def intake():
    for i in range(n):
        for j in range(n):
            if special[i][j]:
                grid[i][j] += 1

def grow():
    for i in range(n):
        for j in range(n):
            if special[i][j]:
                cnt = 0
                for kx, ky in [(-1, 1), (1, 1), (1, -1), (-1, -1)]:
                    nx = i + kx
                    ny = j + ky

                    if not in_range(nx, ny):
                        continue

                    if grid[nx][ny] >= 1:
                       cnt += 1

                grid[i][j] += cnt


def cut():
    for i in range(n):
        for j in range(n):
            next_special[i][j] = False

    for i in range(n):
        for j in range(n):
            if not special[i][j] and grid[i][j] >= 2:
                # 높이 2를 벰
                grid[i][j] -= 2

                # 해당 위치에 특수 영양제를 둠
                next_special[i][j] = True

    for i in range(n):
        for j in range(n):
            special[i][j] = next_special[i][j]


for _ in range(m):
    d, p = map(int, input().split())

    # 특수 영양제 이동
    move(d - 1, p)

    # 특수 영양제 투입
    intake()

    # 대각선만큼 더 성장
    grow()

    # 리브로수 벰
    cut()

print(sum([
    grid[i][j]
    for i in range(n)
    for j in range(n)
]))