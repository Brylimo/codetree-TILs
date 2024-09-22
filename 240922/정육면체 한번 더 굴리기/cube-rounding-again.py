from collections import deque

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 주사위의 상태를 배열로 관리
up, down = 1, 6
dice = [5, 3, 2, 4] # 상하좌우
dir = 1

ans = 0
x, y = 0, 0

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    return True

def move():
    global x, y, dir, up, down

    # 현재 방향으로 1칸 이동
    nx = x + dx[dir]
    ny = y + dy[dir]

    if not in_range(nx, ny):
        dir = (dir + 2) % 4

        nx = x + dx[dir]
        ny = y + dy[dir]

    x, y = nx, ny

    # 주사위 상태 변경
    opposite_dir = (dir + 2) % 4

    temp = dice[dir]
    dice[dir] = up
    dice[opposite_dir] = down

    down = temp
    up = 7 - temp

def bfs(x, y, target):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))

    cnt = 1
    while queue:
        ax, ay = queue.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if not in_range(nx, ny):
                continue

            if not visited[nx][ny] and grid[nx][ny] == target:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1

    return cnt

def calculate():
    global ans

    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    target = grid[x][y]
    cnt = bfs(x, y, target)

    ans += cnt * target

def next_dir():
    global dir
    cell = grid[x][y]

    if cell < down:
        dir = (dir + 1) % 4
    elif cell > down:
        dir = (dir + 3) % 4

for _ in range(m):
    # 주사위 한칸 이동
    move()

    # 점수 구하기
    calculate()

    # 방향 설정
    next_dir()

print(ans)