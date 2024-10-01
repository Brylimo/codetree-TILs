n, k = map(int, input().split())
grid = [
    [2] * (n + 2)
    for _ in range(n + 2)
]
smap = [
    [[] for _ in range(n + 2)]
    for _ in range(n + 2)
]

for i in range(1, 1 + n):
    grid[i][1:-1] = map(int, input().split())

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

piece_loc = [0] * (k + 1)
piece_dir = [0] * (k + 1)
for i in range(1, k + 1):
    x, y, d = map(int, input().split())

    piece_loc[i] = (x, y)
    piece_dir[i] = d
    smap[x][y].append(i)

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

def end():
    flag = any([
        True
        for i in range(n)
        for j in range(n)
        if len(smap[i][j]) >= 4
    ])

    if flag:
        return True
    return False

def go(px, py, pdir, i):
    nx = px + dx[pdir]
    ny = py + dy[pdir]

    if grid[nx][ny] == 0:
        flag = False
        ulst = []
        for j, idx in enumerate(smap[px][py]):
            if not flag and idx != i:
                continue
            if idx == i:
                flag = True

            piece_loc[idx] = (nx, ny)
            ulst.append(idx)
            smap[nx][ny].append(idx)

        for u in range(len(ulst)):
            smap[px][py].remove(ulst[u])
    elif grid[nx][ny] == 1:
        tlst = []
        ulst = []
        flag = False
        for j, idx in enumerate(smap[px][py]):
            if not flag and idx != i:
                continue
            if idx == i:
                flag = True

            piece_loc[idx] = (nx, ny)
            ulst.append(idx)
            tlst.append(idx)

        for u in range(len(ulst)):
            smap[px][py].remove(ulst[u])

        for j in tlst[::-1]:
            smap[nx][ny].append(j)
    elif grid[nx][ny] == 2:
        if pdir == 1:
            pdir = 2
        elif pdir == 2:
            pdir = 1
        elif pdir == 3:
            pdir = 4
        elif pdir == 4:
            pdir = 3
        piece_dir[i] = pdir

        nx = px + dx[pdir]
        ny = py + dy[pdir]

        if grid[nx][ny] != 2:
            go(px, py, pdir, i)

turn = 0
while not end():
    # 말 이동
    for i in range(1, k + 1):
        px, py = piece_loc[i]
        pdir = piece_dir[i]

        go(px, py, pdir, i)
        if end():
            break

    turn += 1
    if turn > 1000:
        break

if turn > 1000:
    print(-1)
else:
    print(turn)