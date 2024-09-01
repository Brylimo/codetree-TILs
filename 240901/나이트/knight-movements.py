from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

step = [
    [0] * n
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]

def bfs(x, y):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))

    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    while queue:
        ax, ay = queue.popleft()
        
        for i in range(8):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny]:
                step[nx][ny] = step[ax][ay] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))

bfs(r1 - 1, c1 - 1)

if visited[r2 - 1][c2 - 1]:
    print(step[r2 - 1][c2 - 1])
else:
    print(-1)