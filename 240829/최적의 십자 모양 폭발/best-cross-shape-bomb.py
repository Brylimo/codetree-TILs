from copy import deepcopy

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def bomb(vgrid, x, y):
    # 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0

    bomb_range = vgrid[x][y]

    # bomb
    for i in range(n):
        for j in range(n):
            if (x == i or y == j) and abs(x - i) + abs(y - j) < bomb_range:
                vgrid[i][j] = 0
    
    # fall down
    for j in range(n):
        end_of_temp = n - 1
        for i in range(n - 1, -1, -1):
            if vgrid[i][j]:
                next_grid[end_of_temp][j] = vgrid[i][j]
                end_of_temp -= 1

    # update
    for i in range(n):
        for j in range(n):
            vgrid[i][j] = next_grid[i][j]

def find_pair(vgrid):
    dx = [0, 1]
    dy = [1, 0]

    cnt = 0
    for i in range(n):
        for j in range(n):
            if vgrid[i][j] == 0:
                continue

            for k in range(2):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if vgrid[nx][ny] == vgrid[i][j]:
                    cnt += 1

    return cnt

ans = 0
for i in range(n):
    for j in range(n):
        # deep copy
        vgrid = deepcopy(grid)
        
        # bombing
        bomb(vgrid, i, j)

        # find the # of pairs
        ans = max(ans, find_pair(vgrid))

print(ans)