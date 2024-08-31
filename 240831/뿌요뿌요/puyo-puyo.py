import sys
sys.setrecursionlimit(20000)

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]

def dfs(num, x, y):
    global block_size

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    block_size += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if not visited[nx][ny] and grid[nx][ny] == num:
            visited[nx][ny] = True
            dfs(num, nx, ny)

bomb_num = 0
max_block_size = 0
for num in range(1, 101):
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    for i in range(n):
        for j in range(n):
            block_size = 0
            
            if not visited[i][j] and grid[i][j] == num:
                visited[i][j] = True
                dfs(num, i, j)

                if block_size >= 4:
                    bomb_num += 1

                max_block_size = max(max_block_size, block_size)

print(bomb_num, max_block_size)