n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def simulate(start):
    dir = start // n
    x, y = -1, -1

    # 시작 지점 초기화
    remnant = start % n
    # down
    if dir == 0:
        x = 0
        y = remnant
    
    # left
    elif dir == 1:
        x = remnant
        y = n - 1

    # up
    elif dir == 2:
        x = n - 1
        y = n - remnant - 1

    # right
    elif dir == 3:
        x = n - remnant - 1
        y = 0

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    tick = 0
    while True:
        if tick > 0:
            nx = x + dx[dir]
            ny = y + dy[dir]

            # 종료 조건
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                tick += 1
                break
        else:
            nx = x
            ny = y

        # / 모양
        if grid[nx][ny] == 1:    
            if dir == 0 or dir == 2:
                dir = (dir + 1) % 4
            else:
                dir = (dir + 3) % 4

            tick += 1
        # \ 모양
        elif grid[nx][ny] == 2:    
            if dir == 0 or dir == 2:
                dir = (dir + 3) % 4
            else:
                dir = (dir + 1) % 4

            tick += 1
        # 그냥 직진
        else:
            tick += 1

        x, y = nx, ny

    return tick

ans = 0
for i in range(4 * n):
    ans = max(ans, simulate(i))

print(ans)