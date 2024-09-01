from collections import deque

n, k, u, d = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]

ans = 0

def bfs(x, y):
    queue = deque([])

    # 시작 도시 방문처리
    visited[x][y] = True
    queue.append((x, y))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        ax, ay = queue.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and u <= abs(grid[nx][ny] - grid[ax][ay]) <= d:
                visited[nx][ny] = True
                queue.append((nx, ny))

def move():
    global ans

    # visited 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    # 큐에 도시들을 집어넣음
    for candidate in candidates:
        cx, cy = candidate

        if not visited[cx][cy]:
            # 도시간 이동
            bfs(cx, cy)

    sum_val = sum([
        1
        for i in range(n)
        for j in range(n)
        if visited[i][j]
    ])

    ans = max(ans, sum_val)

def show():
    for i in range(n):
        print(visited[i])
    print()

candidates = []
# backtracking으로 k 도시 선택(조합)
def calc(i, j, cnt):
    # 종료조건
    if i == n:
        if cnt == k:
            move()
        return

    # 종료조건
    if cnt == k:
        move()
        return

    candidates.append((i, j))
    if j == n - 1:
        calc(i + 1, 0, cnt + 1)
    else:
        calc(i, j + 1, cnt + 1)
    candidates.pop()

    if j == n - 1:
        calc(i + 1, 0, cnt)
    else:
        calc(i, j + 1, cnt)


calc(0, 0, 0)

print(ans)