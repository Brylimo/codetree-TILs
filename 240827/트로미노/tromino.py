n, m = map(int, input().split())

grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

dx = [
    [0, -1, -2],
    [0, 0, 0],
    [0, -1, -1],
    [0, 0, -1],
    [-1, -1, 0],
    [0, 0, -1]
]
dy = [
    [0, 0, 0],
    [0, 1, 2],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 1]
]

ans = 0
for i in range(n):
    for j in range(m):
        for k in range(6):
            sum_val = 0
            flag = True
            for h in range(3):
                nx = i + dx[k][h]
                ny = j + dy[k][h]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    flag = False
                    break

                sum_val += grid[nx][ny]

            if flag:
                ans = max(ans, sum_val)

print(ans)