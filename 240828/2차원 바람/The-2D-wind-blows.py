n, m, q = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

def simulate(r1, c1, r2, c2):
    up = grid[r1][c1:c2 + 1]
    down = grid[r2][c1:c2 + 1]
    left = []
    for i in range(r1, r2 + 1):
        left.append(grid[i][c1])
    right = []
    for i in range(r1, r2 + 1):
        right.append(grid[i][c2])

    # rotate
    up_temp = up[-2]
    for i in range(len(up) - 1, 0, -1):
        up[i] = up[i - 1]
    up[0] = left[1]

    right_temp = right[-2]
    for i in range(len(right) - 1, 0, -1):
        right[i] = right[i - 1]
    right[0] = up_temp

    down_temp = down[1]
    for i in range(len(down) - 1):
        down[i] = down[i + 1]
    down[-1] = right_temp

    for i in range(len(left) - 1):
        left[i] = left[i + 1]
    left[-1] = down_temp

    for i in range(c1, c2 + 1):
        grid[r1][i] = up[i - c1]

    for i in range(c1, c2 + 1):
        grid[r2][i] = down[i - c1]

    for i in range(r1, r2 + 1):
        grid[i][c2] = right[i - r1]

    for i in range(r1, r2 + 1):
        grid[i][c1] = left[i - r1]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    temp = [[0] * m for _ in range(n)]
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            sum_val = grid[i][j]
            cnt = 1

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue                

                sum_val += grid[nx][ny]
                cnt += 1

            average = int(sum_val / cnt)

            temp[i][j] = average

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            grid[i][j] = temp[i][j]

for i in range(q):
    r1, c1, r2, c2 = map(int, input().split())

    simulate(r1 - 1, c1 - 1, r2 - 1, c2 - 1)

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()