n = int(input())
OFFSET = 100
MAX_R = 201

grid = [[0] * MAX_R for _ in range(MAX_R)]
for k in range(1, n+1):
    colors = [1, 2]
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i + OFFSET][j + OFFSET] = colors[k % 2]

area = 0
for i in range(MAX_R):
    for j in range(MAX_R):
        if grid[i][j] == 1:
            area += 1

print(area)