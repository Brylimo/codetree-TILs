r, c = map(int, input().split())
grid = []

black_pos = []
for i in range(r):
    grid.append(list(input().split()))
    for j in range(c):
        if grid[i][j] == 'B':
            black_pos.append((i, j))

cnt = 0
x, y = 0, 0
if grid[x][y] == 'W':
    for bx, by in black_pos:
        if bx >= r - 2 or by >= c - 2:
            continue

        for i in range(bx + 1, r - 1):
            for j in range(by + 1, c - 1):
                if grid[i][j] == 'W':
                    cnt += 1
else:
    for bx, by in black_pos:
        if bx >= r - 1 or by >= c - 1:
            continue

        for i in range(1, bx):
            for j in range(1, by):
                if grid[i][j] == 'W':
                    cnt += 1
print(cnt)