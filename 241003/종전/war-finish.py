import sys
INT_MAX = sys.maxsize

EMPTY = (-1, -1)

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
country = [
    [0] * n
    for _ in range(n)
]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

def create_country(dl, dr, ul, ur):
    # 초기화
    for i in range(n):
        for j in range(n):
            country[i][j] = 0

    country[dl[0]][dl[1]] = 1
    country[dr[0]][dr[1]] = 1
    country[ul[0]][ul[1]] = 1
    country[ur[0]][ur[1]] = 1

    for i in range(n):
        for j in range(n):
            if country[i][j] != 0:
                continue

            if ur[0] < i < dl[0] and ul[1] < j < dr[1]:
                country[i][j] = 1
            # 2의 나라
            elif ul[0] > i and j <= ur[1]:
                country[i][j] = 2
            elif dr[0] >= i and j > ur[1]: # 3의 나라
                country[i][j] = 3
            elif ul[0] <= i and j < dl[1]: # 4의 나라
                country[i][j] = 4
            elif dr[0] < i and j >= dl[1]: # 5의 나라
                country[i][j] = 5
            else:
                country[i][j] = 1

ans = INT_MAX
def calculate():
    global ans

    slst = [0] * 6

    for i in range(n):
        for j in range(n):
            if country[i][j] == 1:
                slst[1] += grid[i][j]
            elif country[i][j] == 2:
                slst[2] += grid[i][j]
            elif country[i][j] == 3:
                slst[3] += grid[i][j]
            elif country[i][j] == 4:
                slst[4] += grid[i][j]
            elif country[i][j] == 5:
                slst[5] += grid[i][j]

    max_val = max(slst[1:])
    min_val = min(slst[1:])

    ans = min(ans, max_val - min_val)

def draw_line():
    dx = [-1, -1, 1, 1]
    dy = [1, -1, -1, 1]

    # 완전 탐색
    for i in range(n):
        for j in range(n):
            x, y = i, j
            for t in range(1, n):
                dl, dr, ul, ur = EMPTY, EMPTY, EMPTY, EMPTY
                for k in range(4):
                    nx = x + dx[k] * t
                    ny = y + dy[k] * t

                    if not in_range(nx, ny):
                        break

                    if k == 0:
                        dr = (nx, ny)
                    elif k == 1:
                        ur = (nx, ny)
                    elif k == 2:
                        ul = (nx, ny)
                    elif k == 3:
                        dl = (nx, ny)
                    x, y = nx, ny

                if dl == EMPTY or dr == EMPTY or ul == EMPTY or ur == EMPTY:
                    break

                create_country(dl, dr, ul, ur)
                calculate()

for i in range(n):
    for j in range(n):
        draw_line()

print(ans)