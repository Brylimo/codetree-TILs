from collections import deque
import heapq
k, m = map(int, input().split())

n = 5
grid = [
    list(map(int, input().split()))
    for _ in range(5)
]
next_grid = [
    [0] * 5
    for _ in range(5)
]
visited = [
    [False] * 5
    for _ in range(5)
]
sub = [
    [0] * 3
    for _ in range(3)
]
next_sub = [
    [0] * 3
    for _ in range(3)
]
wall = list(map(int, input().split()))

heap = []

def show_sub():
    for i in range(3):
        print(sub[i])
    print()

def show():
    for i in range(n):
        print(next_grid[i])
    print()

def showr():
    for i in range(n):
        print(grid[i])
    print()

def rotate(degree):
    for p in range(degree + 1):
        for i in range(3):
            for j in range(3):
                next_sub[i][j] = sub[3 - j - 1][i]

        for i in range(3):
            for j in range(3):
                sub[i][j] = next_sub[i][j]

def fill_sub(x, y, degree):
    for i in range(3):
        for j in range(3):
            sub[i][j] = grid[x + i][y + j]

    rotate(degree)

def explore():

    for i in range(n - 2):
        for j in range(n - 2):
            for d in range(3):
                # sub grid에 값을 채움
                fill_sub(i, j, d)

                # 값을 계산 집어넣음
                calc(i, j, d)

    cost, degree, x, y = heapq.heappop(heap)
    cost = -cost

    if cost == 0:
        return 0

    fill_sub(x, y, degree)

    # grid에 탐사결과 반영
    for i in range(3):
        for j in range(3):
            grid[x + i][y + j] = sub[i][j]

    ans = 0
    while True:
        for i in range(n):
            for j in range(n):
                visited[i][j] = False

        # 실제 값을 채굴
        for i in range(5):
            for j in range(5):
                if not visited[i][j]:
                    ans += dig(i, j)

        # 유적 벽면 값 넣기
        flag = construct()

        if not flag:
            break

    return ans

def construct():
    flag = False
    for j in range(n):
        for i in range(n - 1, -1, -1):
            if grid[i][j] == 0:
                if len(wall) >= 1:
                    flag = True
                    w = wall.pop(0)
                    grid[i][j] = w

    return flag

def dig(x, y):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))

    value = grid[x][y]
    candidates = [(x, y)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        ax, ay = queue.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and grid[nx][ny] == value:
                visited[nx][ny] = True
                queue.append((nx, ny))
                candidates.append((nx, ny))

    cnt = len(candidates)
    if cnt >= 3:
        # 실제 채굴
        for cx, cy in candidates:
            grid[cx][cy] = 0  
    else:
        cnt = 0

    return cnt

def bfs(x, y):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))

    cnt = 0
    value = next_grid[x][y]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        ax, ay = queue.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and next_grid[nx][ny] == value:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1

    if cnt >= 2:
        cnt += 1
    else:
        cnt = 0

    return cnt

def calc(x, y, degree):
    # 그리드 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[i][j]    
            visited[i][j] = False

    # 그리드 완성
    for i in range(3):
        for j in range(3):
            next_grid[x + i][y + j] = sub[i][j]

    # 값 계산
    cost = 0
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                cost += bfs(i, j)

    heapq.heappush(heap, (-cost, degree, x, y))

def turn():
    ans = explore()

    if ans > 0:
        print(ans, end=" ")

for _ in range(k):
    # 첫번째 턴 진행
    turn()
    heap = []