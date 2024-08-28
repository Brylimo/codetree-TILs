n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

r, c = map(int, input().split())

num = grid[r - 1][c - 1]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = r - 1, c - 1

grid[x][y] = 0
for i in range(4):
    for j in range(num - 1):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >=n:
            continue

        grid[nx][ny] = 0
        x, y = nx, ny

    x, y = r - 1, c - 1

temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for j in range(n):
    end_of_temp = n - 1
    for i in range(n-1, -1, -1):
        if grid[i][j] != 0:
            temp[end_of_temp][j] = grid[i][j]
            end_of_temp -= 1

for i in range(n):
    for j in range(n):
        print(temp[i][j], end=" ")
    print()