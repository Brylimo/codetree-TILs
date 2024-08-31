from collections import deque

n, k, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]
visited = [
    [False] * n 
    for _ in range(n)
]
starts = []
for _ in range(k):
    r, c = map(int, input().split())
    starts.append((r - 1, c - 1))

stones = []
# 돌멩이의 위치를 모두 기록
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            stones.append((i, j))

def prave():
    # next_grid 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0

    for x, y in candidates:
        next_grid[x][y] = 1

def bfs(x, y):
    queue = deque([])
    visited[x][y] = True
    queue.append((x, y))

    dx = [-1, 0, 1 ,0]
    dy = [0, 1, 0, -1]

    while queue:
        ax, ay = queue.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and next_grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

def get_num_of_visit():
    # 돌멩이 치우기
    prave()

    for sx, sy in starts:
        if not visited[sx][sy] and next_grid[sx][sy] == 0:
            bfs(sx, sy)

    cnt = sum([
        1
        for i in range(n)
        for j in range(n)
        if visited[i][j]
    ])

    # visited 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    return cnt

ans = 0
candidates = []
# 돌멩이 고르기(조합 - 백트래킹)
def calculate(idx, cnt):
    global ans

    if idx == len(stones):
        if len(candidates) == len(stones) - m:
            ans = max(ans, get_num_of_visit())     
        return

    if len(candidates) == len(stones) - m:
        ans = max(ans, get_num_of_visit())
        return

    candidates.append(stones[idx])
    calculate(idx + 1, cnt + 1)
    candidates.pop()

    calculate(idx + 1, cnt)

calculate(0, 0)
print(ans)