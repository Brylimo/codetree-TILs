n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False] * m
    for _ in range(n)
]

def dfs(x, y, visited, h):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if not visited[nx][ny] and grid[nx][ny] > h:
            visited[nx][ny] = True
            dfs(nx, ny, visited, h)

array = []
for h in range(1, 101):
    # visited 배열 초기화
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

    safe_cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > h and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j, visited, h) 
                safe_cnt += 1

    array.append((-safe_cnt, h))

array.sort()
print(array[0][1], -array[0][0])