import sys
from collections import deque

n, m, k = map(int, input().split())
cur_x, cur_y, tail_x, tail_y, tick = 1, 1, 1, 1, 0

queue = deque([])

apples = []
for _ in range(m):
    x, y = map(int, input().split())
    apples.append((x, y))

movements = []
for _ in range(k):
    d, p = input().split()
    movements.append((d, int(p)))

grid = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

def in_range(x, y):
    if 1 <= x <= n and 1 <= y <= n:
        return True

    return False

def snake_update():
    global tail_x, tail_y

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    # tail 삭제
    grid[tail_x][tail_y] = 0

    # tail 정보 업데이트
    tail_direction = queue.popleft()

    nx = tail_x + dx[tail_direction]
    ny = tail_y + dy[tail_direction]

    if in_range(nx, ny):
        tail_x = nx
        tail_y = ny

def move(direction, p):
    global cur_x, cur_y, tick

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    for _ in range(p):
        queue.append(direction)

        nx = cur_x + dx[direction]
        ny = cur_y + dy[direction]

        if in_range(nx, ny):
            # 사과 존재 x
            if grid[nx][ny] != 2:
                snake_update()

            cur_x = nx
            cur_y = ny

            tick += 1

            # 자기 자신과 충돌
            if grid[nx][ny] == 1:
                print(tick)
                sys.exit(0)

            grid[nx][ny] = 1
        else:
            tick += 1
            print(tick)
            sys.exit(0)

for x, y in apples:
    grid[x][y] = 2
grid[1][1] = 1

dir_dict = {
    'U': 0,
    'D': 1,
    'R': 2,
    'L': 3
}

for d, p in movements:
    move(dir_dict[d], p)

print(tick)