from collections import deque

TAXI = 401

n, m, c = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
tmap = [
    [0] * n
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]
step = [
    [0] * n
    for _ in range(n)
]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

eex, eey = map(int, input().split())
eex, eey = eex - 1, eey - 1

tmap[eex][eey] = TAXI
alive = [True] * (m + 1)

start_point = dict()
end_point = dict()

queue = deque()
passenger = []
for i in range(1, m + 1):
    sx, sy, ex, ey = map(int, input().split())
    sx, sy, ex, ey = sx - 1, sy - 1, ex - 1, ey - 1

    tmap[sx][sy] = i
    tmap[ex][ey] = -i

    start_point[i] = (sx, sy)
    end_point[i] = (ex, ey)

    passenger.append((sx, sy, i))

def end():
    global c

    if c <= 0:
        c = -1
        return True

    flag = True
    for i in range(1, m + 1):
        if alive[i]:
            flag = False
            break

    if flag:
        return True

    return False

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    return True

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not in_range(nx, ny):
                continue

            if not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                step[nx][ny] = step[x][y]
                queue.append((nx, ny))

def find_distance():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not in_range(nx, ny):
                continue

            if not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                queue.append((nx, ny))

def find():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0

    for i, (sx, sy, id) in enumerate(passenger):
        # 해당 승객이 살아 있으면
        if alive[id]:
            visited[sx][sy] = True
            step[sx][sy] = id
            queue.append((sx, sy))

    bfs()
    pid = step[eex][eey]

    return pid

def move(id):
    global c, eex, eey

    # 초기화
    for i in range(n):
        for j in range(n):
            step[i][j] = 0
            visited[i][j] = False

    # 거리 구하기
    queue.append((start_point[id][0], start_point[id][1]))
    visited[start_point[id][0]][start_point[id][1]] = True
    find_distance()

    dist = step[eex][eey]

    tmap[eex][eey] = 0
    tmap[start_point[pid][0]][start_point[pid][1]] = TAXI
    c -= dist

    eex, eey = start_point[pid][0], start_point[pid][1]

    if c <= 0:
        c = 0

def move_dist(id):
    global c, eex, eey

    # 초기화
    for i in range(n):
        for j in range(n):
            step[i][j] = 0
            visited[i][j] = False

    # 거리 구하기
    queue.append((start_point[id][0], start_point[id][1]))
    visited[start_point[id][0]][start_point[id][1]] = True
    find_distance()

    dist = step[end_point[id][0]][end_point[id][1]]

    if dist == 0:
        c = -1
        return

    tmap[start_point[id][0]][start_point[id][1]] = 0
    tmap[end_point[pid][0]][end_point[pid][1]] = TAXI
    c -= dist

    eex, eey = end_point[pid][0], end_point[pid][1]

    if c < 0:
        c = 0
        return

    # 충전
    c += dist * 2
    alive[id] = False

def init():
    # passenger 소팅
    passenger.sort()

init()
while not end():
    # 가장 가까운 승객을 찾음
    pid = find()

    if pid == 0:
        c = -1
        break

    # 해당 승객한테 이동
    move(pid)

    if end():
        break

    # 도착지로 이동
    move_dist(pid)

    if end():
        break

print(c)