from collections import deque

n = int(input())
t = 3 # 3 회전

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0] * n
    for _ in range(n)
]
painting = [
    [0] * n
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0
class Group:
    def __init__(self, num, cnt, foes):
        self.num = num
        self.cnt = cnt
        self.foes = foes

def show():
    for i in range(n):
        print(grid[i])
    print()

def show_paint():
    for i in range(n):
        print(painting[i])
    print()

def is_inrange(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    return True

def bfs(x, y, lion_cnt):
    global groups

    queue = deque()
    visited[x][y] = True
    queue.append((x, y))

    cnt = 1
    num = grid[x][y]
    group = painting[x][y]

    foes = [0] * lion_cnt
    while queue:
        ax, ay = queue.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if not is_inrange(nx, ny):
                continue

            if not visited[nx][ny] and painting[nx][ny] == group:
                visited[nx][ny] = True
                cnt += 1
                queue.append((nx, ny))

            # 맞닿아 있는 다른 타일
            if painting[nx][ny] != group:
                foes[painting[nx][ny]] += 1

    # 정산
    groups[group] = Group(num, cnt, foes)

def init(x, y, group_cnt):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))

    num = grid[x][y]
    painting[x][y] = group_cnt
    while queue:
        ax, ay = queue.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if not is_inrange(nx, ny):
                continue

            if not visited[nx][ny] and grid[nx][ny] == num:
                visited[nx][ny] = True
                queue.append((nx, ny))
                painting[nx][ny] = group_cnt

def score(lion_cnt):
    global ans

    # 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, lion_cnt)

    # 점수 구하기
    for i in range(lion_cnt - 1):
        for j in range(i + 1, lion_cnt):
            ans += (groups[i].cnt + groups[j].cnt) * groups[i].num * groups[j].num * groups[i].foes[j]

def cross_rotate():
    total = n // 2

    for i in range(total):
        # 회전 진행
        temp = grid[i][total]
        next_grid[i][total] = grid[total][n - i - 1]
        next_grid[total][n - i - 1] = grid[n - i - 1][total]
        next_grid[n - i - 1][total] = next_grid[total][i]
        next_grid[total][i] = temp

def square_rotate():
    total = n // 2

    px = [0, 0, 1, 1]
    py = [0, 1, 0, 1]

    for k in range(4):
        x, y = px[k] * (total + 1), py[k] * (total + 1)
        t = total

        for i in range(total):
            for j in range(total):
                next_grid[x + i][y + j] = grid[x + t - j - 1][y + i]

def rotate():
    # 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[i][j]

    # 십자 모양 회전
    cross_rotate()

    # 정사각형 회전
    square_rotate()

    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

# 초기화
group_cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            init(i, j, group_cnt)
            group_cnt += 1

groups = [None] * group_cnt

# 초기 조화로움 점수 구하기
score(group_cnt)

for i in range(3):
    # 회전
    rotate()

    # painting 표시
    for a in range(n):
        for b in range(n):
            visited[a][b] = False

    pro_cnt = 0
    for a in range(n):
        for b in range(n):
            if not visited[a][b]:
                init(a, b, pro_cnt)
                pro_cnt += 1

    groups = [None] * pro_cnt

    # 조화로움 점수 구하기
    score(pro_cnt)

print(ans)