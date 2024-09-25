from collections import deque

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0] * n
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

def bfs(x, y):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))

    blst = [(1, -x, y)]
    group_cnt = 1
    red_bomb_cnt = 0
    while queue:
        ax, ay = queue.popleft()
        color = grid[ax][ay]

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if not in_range(nx, ny):
                continue

            if not visited[nx][ny] and (color == grid[nx][ny] or grid[nx][ny] == 0):
                if grid[nx][ny] == 0:
                    red_bomb_cnt += 1
                    blst.append((10, -nx, ny))
                else:
                    blst.append((1, -nx, ny))
                    visited[nx][ny] = True

                group_cnt += 1

                queue.append((nx, ny))

    blst.sort()
    _, norm_x, norm_y = blst[0]

    return (-group_cnt, red_bomb_cnt, norm_x, norm_y, blst)

def find_bombs_group():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    candidates = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and 1 <= grid[i][j] <= m:
                t = bfs(i, j)
                candidates.append(t)

    if len(candidates) > 0:
        candidates.sort()
        largest_bomb_group = candidates[0]
        group_cnt = -largest_bomb_group[0]

        if group_cnt < 2:
            return None

        return largest_bomb_group
    else:
        return None

def remove_bombs(bomb_group):
    group_cnt, red_bomb_cnt, norm_x, norm_y, blst = bomb_group

    if blst:
        for _, x, y in blst:
            grid[-x][y] = -2 # -2 : void

def gravity():
    # 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = -2

    for j in range(n):
        idx = n - 1
        for i in range(n - 1, -1, -1):
            # 검정색 돌
            if grid[i][j] == -1:
                next_grid[i][j] = grid[i][j]
                idx = i

            if grid[i][j] != -2:
                next_grid[idx][j] = grid[i][j]
                idx -= 1

    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

def rotate_grid():
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = -2

    for _ in range(3):
        for i in range(n):
            for j in range(n):
                next_grid[i][j] = grid[j][n - i - 1]

    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

ans = 0
time = 0
while True:
    # 가장 큰 폭탄 묶음 찾음
    largest_bomb_group = find_bombs_group()

    if largest_bomb_group is None:
        break

    # 폭탄 묶음 제거
    remove_bombs(largest_bomb_group)

    # 중력
    gravity()

    # 격자판 반시계 90도 회전
    rotate_grid()

    # 중력
    gravity()

    time += 1

    C = -largest_bomb_group[0]
    ans += C * C

print(ans)