n, m, t = map(int, input().split())
marbles = []
next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dir_dict = {
    'U': 0,
    'L': 1,
    'R': 2,
    'D': 3
}

for i in range(1, m + 1):
    r, c, d, w = input().split()
    r, c, w = map(int, [r, c, w])

    marbles.append((r - 1, c - 1, dir_dict[d], w, i))

def next_point(marble):
    x, y, dir, w, idx = marble
    
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        dir = 3 - dir
        return (x, y, dir)

    x, y = nx, ny

    return (x, y, dir)

def move_all():
    global marbles

    # next_grid 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0

    for marble in marbles:
        _, _, _, w, idx = marble

        # 다음 이동할 위치 계산
        x, y, dir = next_point(marble)

        # 이미 구슬이 있음
        if next_grid[x][y] != 0:
            p_idx, p_w, p_dir = next_grid[x][y]

            if p_idx > idx:
                next_grid[x][y] = (p_idx, w + p_w, p_dir)
            else:
                next_grid[x][y] = (idx, w + p_w, dir)
        # 구슬이 존재하지 않음  
        else:
            next_grid[x][y] = (idx, w, dir)
                
    next_marbles = []
    for i in range(n):
        for j in range(n):
            if next_grid[i][j] != 0:
                idx, w, dir = next_grid[i][j]

                next_marbles.append((i, j, dir, w, idx))

    marbles = next_marbles[:]

for _ in range(t):
    move_all()

marble_length = len(marbles)
print(marble_length, end=" ")

max_weight = max([
    marbles[i][3]
    for i in range(marble_length)
])
print(max_weight)