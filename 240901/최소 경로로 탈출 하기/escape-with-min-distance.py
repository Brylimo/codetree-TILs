from collections import deque

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
step = [
    [0] * m
    for _ in range(n)
]
visited = [
    [False] * m
    for _ in range(n)
]

queue = deque()

def bfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        ax, ay = queue.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny] and grid[nx][ny] == 1:
                step[nx][ny] = step[ax][ay] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))

queue.append((0, 0))
visited[0][0] = True

bfs(0, 0)

if not step[n - 1][m - 1]:
    print(-1)
else:
    print(step[n - 1][m - 1])