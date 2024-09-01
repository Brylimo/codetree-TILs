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
steps = [
    [0] * n 
    for _ in range(n)
]

def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and grid[nx][ny]:
                steps[nx][ny] = steps[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))

# 상한 귤 저장
rottens = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == 2
]
queue = deque(rottens)
for rx, ry in rottens:
    visited[rx][ry] = True

bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            print(-1, end=" ")
        else:
            if not visited[i][j]:
                print(-2, end=" ")
            else:
                print(steps[i][j], end=" ")
    print()