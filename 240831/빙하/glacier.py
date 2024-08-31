from collections import deque

NOT_VISITED = -1

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [NOT_VISITED] * m 
    for _ in range(n)
]

tick = 0
targets = deque([])
prev = 0

# 가장자리 체크
def check_corners(x, y):
    global tick

    queue = deque([])
    visited[x][y] = tick
    grid[x][y] = -1
    queue.append((x, y))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        ax, ay = queue.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if visited[nx][ny] == NOT_VISITED and grid[nx][ny] == 0:
                visited[nx][ny] = tick
                grid[nx][ny] = -1
                queue.append((nx, ny))

def melt(x, y):
    global tick, prev

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while targets:
        ax, ay = targets.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if visited[nx][ny] == NOT_VISITED:
                if grid[nx][ny] == 0:
                    targets.append((nx, ny))
                else:
                    prev += 1
                visited[nx][ny] = tick
                grid[nx][ny] = -1

def show():
    for i in range(n):
        print(visited[i])
    print()

# 가장자리 모두 방문처리
check_corners(0, 0)

while True:
    total = sum([
        grid[i][j]
        for i in range(n)
        for j in range(m)
    ])

    # 종료 조건
    if total == -(n*m):
        break

    tick += 1
    prev = 0

    for i in range(n):
        for j in range(m):
            if visited[i][j] == tick - 1:
                targets.append((i, j))

    melt(i, j)

print(tick, prev)