n, m, cur_x, cur_y = map(int, input().split())

cur_x -= 1
cur_y -= 1

dirs = list(input().split())
grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

up = 5
down = 2
left = 4
right = 3

score = 6
dir = 'V'

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    return True

def simulate(next_dir):
    global cur_x, cur_y, dir, up, down, left, right, score

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    grid[cur_x][cur_y] = score

    if next_dir == 'L':
        nx = cur_x + dx[3]
        ny = cur_y + dy[3]

        if not in_range(nx, ny):
            return

        right = score
        score = left
        left = 7 - right
    elif next_dir == 'R':
        nx = cur_x + dx[1]
        ny = cur_y + dy[1]

        if not in_range(nx, ny):
            return

        left = score
        score = right
        right = 7 - left
    elif next_dir == 'U':
        nx = cur_x + dx[0]
        ny = cur_y + dy[0]

        if not in_range(nx, ny):
            return

        down = score
        score = up
        up = 7 - down
    elif next_dir == 'D':
        nx = cur_x + dx[2]
        ny = cur_y + dy[2]

        if not in_range(nx, ny):
            return

        up = score
        score = down
        down = 7 - up

    cur_x = nx
    cur_y = ny

for next_dir in dirs:
    simulate(next_dir)

simulate('U')

ans = sum([
    grid[i][j]
    for i in range(n)
    for j in range(n)
])

print(ans)