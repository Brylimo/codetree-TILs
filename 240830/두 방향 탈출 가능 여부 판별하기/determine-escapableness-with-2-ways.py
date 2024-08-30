n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False] * m 
    for _ in range(n)
]

ans = False
def dfs(x, y):
    global ans
    
    dx = [0, 1]
    dy = [1, 0]

    if x == n - 1 and y == m - 1:
        ans = True
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if grid[nx][ny] == 0:
            continue
        
        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)

visited[0][0] = True
dfs(0, 0)
if ans:
    print(1)
else:
    print(0)