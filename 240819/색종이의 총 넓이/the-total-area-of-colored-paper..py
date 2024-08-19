n = int(input())
OFFSET = 100
MAX_R = 201

grid = [[0] * MAX_R for _ in range(MAX_R)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            grid[OFFSET + i][OFFSET + j] += 1

cnt = 0
for i in range(MAX_R):
    for j in range(MAX_R):
        if grid[i][j] >= 1:
            cnt += 1

print(cnt)