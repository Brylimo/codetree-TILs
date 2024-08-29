n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

for i in range(1, n):
    flag = False
    for j in range(k - 1, k + m - 1):
        if grid[i][j] == 1:
            flag = True
            break

    if flag:
        for j in range(k - 1, k + m - 1):
            grid[i - 1][j] = 1
        break
        

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()