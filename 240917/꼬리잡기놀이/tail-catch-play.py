from collections import deque

n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]
steps = [
    [0] * n 
    for _ in range(n)
]

ans = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def show():
    for i in range(n):
        print(grid[i])
    print()

def is_inrange(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    return True

def walk(x, y):
    queue = deque()

    visited[x][y] = True
    queue.append((x, y))

    remember = (-1, -1)
    while queue:
        ax, ay = queue.popleft()
        # 현재값
        current = grid[ax][ay]

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if not is_inrange(nx, ny):
                continue

            # 팀의 다른 동료
            if not visited[nx][ny] and grid[nx][ny] == 2:
                queue.append((nx, ny))
                visited[nx][ny] = True
            elif current != 1 and grid[nx][ny] == 3:
                grid[ax][ay] = 3
                grid[nx][ny] = 4
                visited[nx][ny] = True
            elif current == 1 and grid[nx][ny] == 3:
                remember = (nx, ny)
                visited[nx][ny] = True
                grid[ax][ay] = 4
            # 이동해야할 칸
            elif grid[nx][ny] == 4:
                visited[nx][ny] = True
                grid[nx][ny] = current
                if grid[ax][ay] != 3:
                    grid[ax][ay] = 4

    if remember != (-1, -1):
        grid[remember[0]][remember[1]] = 1

def move():
    # 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    for i in range(n):
        for j in range(n):
            # 머리사람 발견
            if not visited[i][j] and grid[i][j] == 1:
                walk(i, j)

def check_line_idx(x, y):
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            steps[i][j] = 0

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    steps[x][y] = 1

    idx = -1
    head = (-1, -1)
    tail = (-1, -1)

    flag = False
    while queue:
        ax, ay = queue.popleft()

        if grid[ax][ay] == 1:
            idx = steps[ax][ay]
            head = (ax, ay)
            flag = True

        if grid[ax][ay] == 3:
            tail = (ax, ay)

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if not is_inrange(nx, ny):
                continue

            if not visited[nx][ny] and 1 <= grid[nx][ny] <= 3:
                if grid[nx][ny] == 1:
                    flag = True

                if grid[nx][ny] == 3 and not flag:
                    tail = (ax, ay)
                    continue

                visited[nx][ny] = True
                steps[nx][ny] = steps[ax][ay] + 1
                queue.append((nx, ny))
    
    return (idx, head, tail)

def cannon(i):
    global ans

    # 초기값 설정
    sx, sy, dir = -1, -1, -1
    i = i % (4 * n)

    if i < n:
        dir = 1

        sx, sy = i % n, 0
    elif n <= i < 2 * n:
        dir = 0

        sx, sy = n - 1, i % n
    elif 2 * n <= i < 3 * n:
        dir = 3

        sx, sy = n - (i % n) - 1, n - 1
    elif 3 * n <= i < 4 * n:
        dir = 2

        sx, sy = 0, n - (i % n) - 1

    # 첫 칸 확인
    if is_inrange(sx, sy):
        if 1 <= grid[sx][sy] <= 3:
            # 몇번째인지 확인
            idx, head, tail = check_line_idx(sx, sy)

            # 점수 획득
            ans += idx ** 2

            # 방향 반대로 만들기
            hx, hy = head
            tx, ty = tail

            grid[hx][hy] = 3
            grid[tx][ty] = 1

            return

    for j in range(n):
        nx = sx + dx[dir]
        ny = sy + dy[dir]

        if is_inrange(nx, ny):
            if 1 <= grid[nx][ny] <= 3:
                # 몇번째인지 확인
                idx, head, tail = check_line_idx(nx, ny)

                # 점수 획득
                ans += idx ** 2

                # 방향 반대로 만들기
                hx, hy = head
                tx, ty = tail

                grid[hx][hy] = 3
                grid[tx][ty] = 1

                break

        sx, sy = nx, ny

for i in range(k):
    # 모든 팀이 움직임
    move()

    # 공이 던져짐
    cannon(i)

    #show()
    #print(ans)

print(ans)