n, m = map(int, input().split())
grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]

numbers = [None] * 401
for i in range(n):
    given_nums = list(map(int, input().split()))
    for j, num in enumerate(given_nums):
        grid[i][j].append(num)
        numbers[num] = (i, j)

orders = list(map(int, input().split()))

def get_floor_of_cell(value, x, y):
    end = len(grid[x][y])
    index = 0

    for i, v in enumerate(grid[x][y]):
        if v == value:
            index = i
            break

    return index

def move(num):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    cur_x, cur_y = numbers[num]
    num_of_empty = 0

    max_val = 0
    max_pos = (-1, -1)
    for i in range(8):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            num_of_empty += 1
            continue

        if len(grid[nx][ny]) == 0:
            num_of_empty += 1
            continue

        if max_val < max(grid[nx][ny]):
            max_val = max(grid[nx][ny])
            max_pos = (nx,ny)

    if num_of_empty == 8:
        return

    dest_x, dest_y = max_pos[0], max_pos[1]

    floor = get_floor_of_cell(num, cur_x, cur_y)
    packs = grid[cur_x][cur_y][:floor + 1]

    del grid[cur_x][cur_y][:floor + 1]

    for pack in packs[::-1]:
        grid[dest_x][dest_y].insert(0, pack)
        numbers[pack] = (dest_x, dest_y)

for order in orders:
    move(order)

for i in range(n):
    for j in range(n):
        if len(grid[i][j]) == 0:
            print("None")
            continue

        for k in range(len(grid[i][j])):
            print(grid[i][j][k], end=" ")
        print()