n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

flag = False
for i in range(1, n):
    for j in range(k - 1, k + m - 1):
        if grid[i][j] == 1:
            flag = True
            break

    if flag:
        for j in range(k - 1, k + m - 1):
            grid[i - 1][j] = 1
        break
        
if n == 1:
    for j in range(k - 1, k + m - 1):
        grid[0][j] = 1

if not flag:
   for j in range(k - 1, k + m - 1):
        grid[n - 1][j] = 1 

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()