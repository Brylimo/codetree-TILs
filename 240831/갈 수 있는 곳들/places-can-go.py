from collections import deque

n, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]

cnt = 0

def bfs(x, y):
    global cnt

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue = deque([])

    if not visited[x][y]:
        queue.append((x, y))

        visited[x][y] = True
        cnt += 1

    while queue:
        ax, ay = queue.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1


for _ in range(k):
    r, c = map(int, input().split())
    bfs(r - 1, c - 1)

print(cnt)