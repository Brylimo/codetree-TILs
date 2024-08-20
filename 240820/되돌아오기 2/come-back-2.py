orders = list(input())

x, y = 0, 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

tick = 1
dir = 0
ans = -1
for order in orders:
    if order == 'R':
        dir = (dir + 1) % 4
    elif order == 'L':
        dir = (dir + 3) % 4
    elif order == 'F':
        nx = x + dx[dir]
        ny = y + dy[dir]

        x, y = nx, ny

    if x == 0 and y == 0:
        ans = tick
        break

    tick += 1

print(ans)