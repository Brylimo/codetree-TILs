from collections import deque

n = 10
grid = []

lx, ly = 0, 0
for i in range(n):
    grid.append(list(input()))
    for j in range(n):
        if grid[i][j] == 'L':
            lx, ly = i, j
            break

ans = 0
visited = [[0] * n for _ in range(n)]
def bfs(x, y):
    global ans
    queue = deque([])
    queue.append((x, y))
    visited[x][y] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        ax, ay = queue.popleft()

        if grid[ax][ay] == 'B':
            ans = visited[ax][ay]
            break

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if (visited[nx][ny] == 0 or (visited[nx][ny] != 0 and visited[nx][ny] > visited[ax][ay] + 1)) and grid[nx][ny] != 'R':
                visited[nx][ny] = visited[ax][ay] + 1
                queue.append((nx, ny))
            
bfs(lx, ly)
print(ans - 2)