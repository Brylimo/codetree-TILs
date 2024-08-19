import sys
OFFSET = 1000
MAX_R = 2001

grid = [[0] * MAX_R for _ in range(MAX_R)]
for k in range(1, 3):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i + OFFSET][j + OFFSET] = k 

max_x = 0
max_y = 0
min_x = sys.maxsize
min_y = sys.maxsize
for i in range(MAX_R):
    for j in range(MAX_R):
        if grid[i][j] == 1:
            max_x = max(max_x, j)
            max_y = max(max_y, i)
            min_x = min(min_x, j)
            min_y = min(min_y, i)

print((max_x - min_x + 1) * (max_y - min_y + 1))