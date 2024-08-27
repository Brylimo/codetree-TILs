from collections import deque
n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

ans = 0
def draw_diamond(x, y):
    global ans

    queue = deque([])
    value = 0

    visited = [[False] * n for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue.append((x, y, 1))

    visited[x][y] = True
    value += grid[x][y]

    cur_level = 0
    cnt = 1
    while queue:
        ax, ay, level = queue.popleft()

        if level != cur_level:
            cur_level = level
            if cnt < value * m:
                ans = max(ans, value)

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                cnt += 1
                continue

            if not visited[nx][ny]:
                visited[nx][ny] = True
                value += grid[nx][ny]
                cnt += 1

                queue.append((nx, ny, level + 1))
        
for i in range(n):
    for j in range(n):
        draw_diamond(i, j)

print(ans)