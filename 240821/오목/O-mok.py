import sys
grid = []
for _ in range(19):
    grid.append(list(map(int, input().split())))

for i in range(19):
    for j in range(19):
        if (grid[i][j] == 1 and grid[i][j + 1] == 1 and grid[i][j + 2] == 1 and grid[i][j + 3] == 1 and grid[i][j + 4] == 1):
            print(1)
            print(i + 1, j + 3)
            sys.exit(0)
        elif (grid[i][j] == 2 and grid[i][j + 1] == 2 and grid[i][j + 2] == 2 and grid[i][j + 3] == 2 and grid[i][j + 4] == 2):
            print(2)
            print(i + 1, j + 3)
            sys.exit(0)
        elif (grid[j][i] == 1 and grid[j + 1][i] == 1 and grid[j + 2][i] == 1 and grid[j + 3][i] == 1 and grid[j + 4][i] == 1):
            print(1)
            print(j + 3, i + 1)
            sys.exit(0)
        elif (grid[j][i] == 2 and grid[j + 1][i] == 2 and grid[j + 2][i] == 2 and grid[j + 3][i] == 2 and grid[j + 4][i] == 2):
            print(2)
            print(j + 3, i + 1)
            sys.exit(0)
        elif (grid[i][j] == 1 and grid[i + 1][j + 1] == 1 and grid[i + 2][j + 2] == 1 and grid[i + 3][j + 3] == 1 and grid[i + 4][j + 4] == 1):
            print(1)
            print(i + 3, j + 3)
            sys.exit(0)
        elif (grid[i][j] == 2 and grid[i + 1][j + 1] == 2 and grid[i + 2][j + 2] == 2 and grid[i + 3][j + 3] == 2 and grid[i + 4][j + 4] == 2):
            print(1)
            print(i + 3, j + 3)
            sys.exit(0)

print(0)