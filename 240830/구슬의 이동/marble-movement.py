n, m, t, k = map(int, input().split())
marbles = []

grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]

dir_dict = {
    'U': 0,
    'L': 1,
    'R': 2,
    'D': 3
}

def move(marble):
    num, cur_x, cur_y, dir, v = marble

    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    if (v, num) not in grid[cur_x][cur_y]:
        return

    # grid에서 현재 구슬 삭제
    grid[cur_x][cur_y].remove((v, num))

    for _ in range(v):
        nx = cur_x + dx[dir]
        ny = cur_y + dy[dir]

        # 벽에 충돌
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            dir = 3 - dir

            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

        cur_x = nx
        cur_y = ny

    # 도착점에 구슬 추가
    grid[cur_x][cur_y].append((v, num))
    marbles.append((num, cur_x, cur_y, dir, v))

def remove_marbles():
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) > 0:
                grid[i][j].sort(reverse = True)
                if len(grid[i][j]) > k:
                    grid[i][j] = grid[i][j][:k]

def move_all():
    marbel_len = len(marbles)
    for _ in range(marbel_len):
        marble = marbles.pop(0)
        move(marble)

    # 지워야하는 구슬 제거
    remove_marbles()

for num in range(m):
    r, c, d, v = input().split()

    grid[int(r) - 1][int(c) - 1].append((int(v), num))
    marbles.append((num, int(r) - 1, int(c) - 1, dir_dict[d], int(v)))

for _ in range(t):
    move_all()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(grid[i][j])

print(ans)