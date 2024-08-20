n = int(input())

x, y = 0, 0
dx = [-1, 0, 1 ,0]
dy = [0, 1, 0, -1]

mapper = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}

flag = True
tick = 1
for _ in range(n):
    direction, distance = input().split()
    for i in range(int(distance)):
        nx = x + dx[mapper[direction]]
        ny = y + dy[mapper[direction]]

        if nx == 0 and ny == 0:
            flag = False
            print(tick)
            break

        x = nx
        y = ny
        tick += 1

    if not flag:
        break

if flag:
    print(-1)