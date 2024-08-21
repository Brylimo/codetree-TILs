n = int(input())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

ans = 0
for i in range(n):
    for j in range(n - 2):
        for a in range(i, n):
            for b in range(j, n - 2):
                if not (i == a and (j <= b < j + 3 or j <= b + 2 < j + 3)): 
                    sum_value = 0
                    sum_value += (grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[a][b] + grid[a][b + 1] + grid[a][b + 2])
                    ans = max(ans, sum_value)

print(ans)