from collections import deque

n, m = map(int, input().split())
grid = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
visited = [
    [False] * (n + 1)
    for _ in range(n + 1)
]
record = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

# 사람의 위치 정보
person_x = [0] * (m + 1)
person_y = [0] * (m + 1)
on_board = [False] * (m + 1)
done_move = [False] * (m + 1)
queue = []

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 초기 입력
for i in range(1, n + 1):
    grid[i][1:] = map(int, input().split())

csvs = [None] + [tuple(map(int, input().split())) for _ in range(m)]

basecamps = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if grid[i][j] == 1:
            basecamps.append((i, j))

# 행과 열이 작은 순으로 정렬
basecamps.sort()
time = 0

def is_inrange(x, y):
    if 1 <= x <= n and 1 <= y <= n:
        return True

    return False

def move():
    global queue

    arrived = []
    for i in range(1, m + 1):
        if on_board[i]:
            # 가고자하는 편의점
            cx, cy = csvs[i]
            sx = person_x[i]
            sy = person_y[i]

            # 초기화
            for a in range(1, n + 1):
                for b in range(1, n + 1):
                    visited[a][b] = False
                    record[a][b] = 0

            queue = deque()
            for j in range(4):
                nx = sx + dx[j]
                ny = sy + dy[j]

                if is_inrange(nx, ny) and grid[nx][ny] != 2:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    record[nx][ny] = j

            # 모든 방향에 대해 최단거리를 구함
            bfs(cx, cy)

            # 최종적인 방향
            dir = record[cx][cy]

            # 해당 방향으로 이동
            px = sx + dx[dir]
            py = sy + dy[dir]

            # 편의점 도착
            if px == cx and py == cy:
                arrived.append((cx, cy))
                done_move[i] = True

            person_x[i] = px
            person_y[i] = py

    # 도착 관련 코드 처리
    for cx, cy in arrived:
        grid[cx][cy] = 2

def bfs(cx, cy):
    while queue:
        x, y = queue.popleft()

        if x == cx and y == cy:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_inrange(nx, ny):
                continue

            if not visited[nx][ny]:
                visited[nx][ny] = True
                record[nx][ny] = record[x][y]
                queue.append((nx, ny))

def basecamp(time):
    global queue

    if time > m:
        return

    # 초기화
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            visited[i][j] = False
            record[i][j] = 0
    # 가고싶은 편의점
    cx, cy = csvs[time]

    queue = deque()
    for idx, (bx, by) in enumerate(basecamps, start = 1):
        # 이미 도착한 bc면 넘어감
        if grid[bx][by] == 2:
            continue

        visited[bx][by] = True
        record[bx][by] = idx
        queue.append((bx, by))

    bfs(cx, cy)
    # 가장 가까운 basecamp idx
    res = record[cx][cy]
    res_x, res_y = basecamps[res - 1]

    # bc 방문표시
    grid[res_x][res_y] = 2

    person_x[time] = res_x
    person_y[time] = res_y

    on_board[time] = True

while True:
    time += 1

    # 사람이 한칸 움직임
    move()

    # 베이스캠프 들어감
    basecamp(time)

    if all(done_move[1:]):
        break

print(time)