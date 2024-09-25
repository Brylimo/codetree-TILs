from collections import deque

n, q = map(int, input().split())
size = 2 ** n

grid = [
    list(map(int, input().split()))
    for _ in range(size)
]
next_grid = [
    [0] * size
    for _ in range(size)
]
visited = [
    [False] * size
    for _ in range(size)
]
query = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def sub_rotate(x, y, lev):
    g_size = 2 ** lev
    s_size = 2 ** (lev - 1)

    for i in range(x, x + g_size):
        for j in range(y, y + g_size):
            if i < x + s_size and j < y + s_size:
                ni, nj = i, j + s_size
            elif i < x + s_size and j >= y + s_size:
                ni, nj = i + s_size, j
            elif i >= x + s_size and j >= y + s_size:
                ni, nj = i, j - s_size
            else:
                ni, nj = i - s_size, j

            next_grid[ni][nj] = grid[i][j]

def rotate(lev):
    if lev <= 0:
        return

    # 초기화
    for i in range(size):
        for j in range(size):
            next_grid[i][j] = 0

    g_size = 2 ** lev
    cnt = size // g_size

    for i in range(cnt):
        for j in range(cnt):
            sub_rotate(i * g_size, j * g_size, lev)

    for i in range(size):
        for j in range(size):
            grid[i][j] = next_grid[i][j]

def in_range(x, y):
    if x < 0 or x >= size or y < 0 or y >= size:
        return False
    return True

def melt():
    # 초기화
    for i in range(size):
        for j in range(size):
            next_grid[i][j] = 0

    for i in range(size):
        for j in range(size):

            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if not in_range(nx, ny):
                    continue

                if grid[nx][ny] > 0:
                    cnt += 1

            if cnt < 3 and grid[i][j] > 0:
                next_grid[i][j] = grid[i][j] - 1
            else:
                next_grid[i][j] = grid[i][j]

    for i in range(size):
        for j in range(size):
            grid[i][j] = next_grid[i][j]

def bfs(x, y):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))

    cnt = 1
    while queue:
        ax, ay = queue.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] > 0:
                visited[nx][ny] = True

                cnt += 1
                queue.append((nx, ny))

    return cnt

def calculate():
    for i in range(size):
        for j in range(size):
            visited[i][j] = False

    max_cnt = 0
    for i in range(size):
        for j in range(size):
            if not visited[i][j] and grid[i][j] > 0:
                max_cnt = max(max_cnt, bfs(i, j))

    return max_cnt


for i in range(q):
    lev = query[i]

    # 회전
    rotate(lev)

    # 녹음
    melt()

ans = sum([
    grid[i][j]
    for i in range(size)
    for j in range(size)
    if grid[i][j] > 0
])
max_cnt = calculate()

print(ans)
print(max_cnt)