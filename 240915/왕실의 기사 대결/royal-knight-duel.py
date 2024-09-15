from collections import deque

l, n, q = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(l)
]
knights = [
    [0] * l
    for _ in range(l)
]
next_knights = [
    [0] * l 
    for _ in range(l)
]
visited = [
    [False] * l 
    for _ in range(l)
]

stamina = [0] * (n + 1)
points = [None] * (n + 1)
alive = [True] * (n + 1)
block_stack = []

initial = [0] * (n + 1)

dx = [-1, 0, 1 ,0]
dy = [0, 1, 0, -1]

def show():
    for i in range(l):
        print(knights[i])
    print()

def nshow():
    for i in range(l):
        print(next_knights[i])
    print()

for idx in range(1, n + 1):
    r, c, h, w, k = map(int, input().split())

    r, c, = r - 1, c - 1

    stamina[idx] = k
    initial[idx] = k
    points[idx] = (r, c, h, w)

    for i in range(h):
        for j in range(w):
            knights[r + i][c + j] = idx

def is_inrange(x, y):
    if x < 0 or x >= l or y < 0 or y >= l:
        return False

    return True

def can_go(queue, dir):
    flag = True

    while queue:
        x, y, idx = queue.popleft()

        nx = x + dx[dir]
        ny = y + dy[dir]

        if is_inrange(nx, ny):
            # 벽이 있음
            if grid[nx][ny] == 2:
                flag = False
                break

            if knights[nx][ny] != idx and knights[nx][ny] > 0:
                ii = knights[nx][ny]
                kr, kc, kh, kw = points[ii]
                block_stack.append(ii)

                for i in range(kh):
                    for j in range(kw):
                        queue.append((kr + i, kc + j, ii))

    return flag

def knight_move(owner, dir):
    # next_knights 초기화
    for i in range(l):
        for j in range(l):
            next_knights[i][j] = knights[i][j]
            visited[i][j] = False

    while block_stack:
        idx = block_stack.pop()

        r, c, h, w = points[idx]

        xx, yy = r, c
        for i in range(h):
            for j in range(w):
                x, y = r + i, c + j

                nx, ny = x + dx[dir], y + dy[dir]

                if x == r and y == c:
                    points[idx] = ((nx, ny, h, w))
                    xx, yy = nx, ny

                if is_inrange(nx, ny):
                    next_knights[nx][ny] = idx
                    visited[nx][ny] = True
                    if not visited[x][y]:
                        next_knights[x][y] = 0
                else:
                    alive[idx] = False

        if idx != owner:
            for i in range(h):
                for j in range(w):
                    if grid[xx + i][yy + j] == 1:
                        stamina[idx] -= 1

            if stamina[idx] <= 0:
                stamina[idx] = 0
                alive[idx] = False

                for i in range(h):
                    for j in range(w):
                        next_knights[xx + i][yy + j] = 0

    for i in range(l):
        for j in range(l):
            knights[i][j] = next_knights[i][j]

def move(idx, dir):
    global block_stack

    r, c, h, w = points[idx]
    queue = deque()

    for i in range(h):
        for j in range(w):
            x, y = r + i, c + j
            queue.append((x, y, idx))

    block_stack.append(idx)
    if can_go(queue, dir):
        knight_move(idx, dir)
    else:
        block_stack = []

for _ in range(q):
    idx, d = map(int, input().split())

    if alive[idx]:
        move(idx, d)

    #show()

ans = 0
for i in range(1, n + 1):
    if alive[i]:
        ans += (initial[i] - stamina[i])

print(ans)