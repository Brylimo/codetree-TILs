n = int(input())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

ans = 0
def draw_rect(x, y):
    global ans
    dx = [-1, -1, 1, 1]
    dy = [1, -1, -1, 1]

    check = [0, 0, 0, 0]
    dir = 0

    sum_val = 0
    ax, ay = x, y

    flag = True
    while True:
        nx = ax + dx[dir]
        ny = ay + dy[dir]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            if check[dir] == 0:
                flag = False
                break
            dir += 1
            if dir == 4:
                break
                
            continue
            
        sum_val += grid[nx][ny]
        check[dir] += 1

        ax, ay = nx, ny

    if flag:
        flag = False
        ans = max(ans, sum_val)

for i in range(n):
    for j in range(n):
        draw_rect(i, j)

print(ans)