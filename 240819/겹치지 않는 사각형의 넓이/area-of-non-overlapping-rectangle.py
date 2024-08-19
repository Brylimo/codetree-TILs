OFFSET = 1000
MAX_R = 2001

grid = [[0] * MAX_R for _ in range(MAX_R)]
for k in range(1, 4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[OFFSET + i][OFFSET +j] = k

cnt = 0
for i in range(MAX_R):
    for j in range(MAX_R):
        if grid[i][j] == 1 or grid[i][j] == 2:
            cnt += 1

print(cnt)