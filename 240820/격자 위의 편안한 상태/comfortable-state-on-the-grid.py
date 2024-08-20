n, m = map(int, input().split())

grid = [[0] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(m):
    r, c = map(int, input().split())

    grid[r - 1][c - 1] = 1

    cnt = 0
    for i in range(4):
        nx = r - 1 + dx[i]
        ny = c - 1 + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if grid[nx][ny] == 1:
            cnt += 1

    if cnt == 3:
        print(1)
    else:
        print(0)