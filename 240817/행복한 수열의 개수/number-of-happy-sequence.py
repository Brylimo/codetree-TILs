n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

cnt = 0
for i in range(n):
    for j in range(n - 1):
        flag = True
        for k in range(m):
            if grid[i][j] != grid[i][j + k]:
                flag = False
                break
        if flag:
            cnt += 1
            break

for j in range(n):
    for i in range(n - 1):
        flag = True
        for k in range(m):
            if grid[i][j] != grid[i + k][j]:
                flag = False
                break
        if flag:
            cnt += 1
            break

print(cnt)