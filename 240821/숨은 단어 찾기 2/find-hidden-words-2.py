n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(input()))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'L':
            for k in range(8):
                x, y = i, j
                words = ['L']
                while True:
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break

                    if grid[nx][ny] == 'E':
                        words.append('E')
                        x,y = nx, ny
                    else:
                        break

                    if ''.join(words) == 'LEE':
                        ans += 1
                        break

print(ans)