t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    grid = [
        [-1 for _ in range(n)]
        for _ in range(n)
    ]
    next_grid = [
        [-1 for _ in range(n)]
        for _ in range(n)
    ]

    dir_dict = {
        "U": 0,
        "R": 1,
        "L": 2,
        "D": 3,
    }

    def move(x, y):
        dx = [-1, 0, 0, 1]
        dy = [0, 1, -1, 0]

        dir = grid[x][y]

        nx = x + dx[dir]
        ny = y + dy[dir]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            # 방향을 바꿈
            dir = 3 - dir
            next_grid[x][y] = dir
            return

        # 이미 구슬이 존재하면 삭제
        if next_grid[nx][ny] != -1:
            next_grid[nx][ny] = -1
        else:
            next_grid[nx][ny] = dir

    def move_all():
        # next_grid 초기화
        for i in range(n):
            for j in range(n):
                next_grid[i][j] = -1

        for i in range(n):
            for j in range(n):
                if grid[i][j] != -1:
                    move(i, j)

        for i in range(n):
            for j in range(n):
                grid[i][j] = next_grid[i][j]

    # 구슬 초기화
    for _ in range(m):
        x, y, d = input().split()
        grid[int(x) - 1][int(y) - 1] = dir_dict[d]
    
    for _ in range(n ** 2):
        move_all()

    ans = sum([
        1
        for i in range(n)
        for j in range(n)
        if grid[i][j] != -1
    ])

    print(ans)