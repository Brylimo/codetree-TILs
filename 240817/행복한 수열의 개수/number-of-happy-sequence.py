n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

cnt = 0
for i in range(n):
    for j in range(n - m + 1):
        flag = True
        for k in range(m):
            if grid[i][j + k] != grid[i][j]:
                flag = False
                break
        if flag:
            cnt += 1
            break

for j in range(n):
    for i in range(n - m + 1):
        flag = True
        for k in range(m):
            if grid[i + k][j] != grid[i][j]:
                flag = False
                break
        if flag:
            cnt += 1
            break

print(cnt)