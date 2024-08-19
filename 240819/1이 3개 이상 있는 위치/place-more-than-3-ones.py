n = int(input())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx = i + dx
            ny = j + dy

            if nx < 0 or nx >= n or ny < 0 or ny >=n:
                continue

            if grid[nx][ny] == 1:
                cnt += 1

        if cnt >=3:
            ans += 1

print(ans)