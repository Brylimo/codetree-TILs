n, m, r, c = map(int, input().split())
grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]
next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def spread(time):
    # temp 복사
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[i][j]

    dist = 2 ** (time - 1)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(n):
        for j in range(n):
            # 해당 위치에 폭탄 존재
            if grid[i][j] == 1:
                for k in range(4):
                    nx = i + dx[k] * dist
                    ny = j + dy[k] * dist

                    # 격자 밖을 벗어나면 pass
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue

                    if next_grid[nx][ny] == 0:
                        next_grid[nx][ny] = 1

    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]
                    
# 초기 폭탄 투하
grid[r - 1][c - 1] = 1
for i in range(1, m + 1):
    spread(i)

ans = sum([
    grid[i][j]
    for i in range(n)
    for j in range(n)
])
print(ans)