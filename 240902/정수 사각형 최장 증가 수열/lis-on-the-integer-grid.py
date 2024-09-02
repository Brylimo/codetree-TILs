from collections import deque

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [0] * n
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]

queue = deque()

def move(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    dp[x][y] = grid[x][y]
    visited[x][y] = True

    queue.append((x, y))

    while queue:
        ax, ay = queue.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if grid[nx][ny] > grid[ax][ay] and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

ans = 0
for i in range(n):
    for j in range(n):
        move(i, j)

        cnt = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j]:
                    cnt += 1

                visited[i][j] = False
                dp[i][j] = False

        ans = max(ans, cnt)

print(ans)