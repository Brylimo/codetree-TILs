from collections import deque

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
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

dx = [-1, 0, 1 ,0]
dy = [0, 1, 0, -1]

hospital = []
# 병원 좌표 기록
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            hospital.append((i, j))

queue = deque()

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

ans = int(1e9)
def bfs():
    global ans

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not in_range(nx, ny):
                continue

            if not visited[nx][ny] and grid[nx][ny] != 1:
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1

                queue.append((nx, ny))

    for hx, hy in hospital:
        step[hx][hy] = 0

candidate = []
def calculate(i, cnt):
    global ans
    if cnt == m:
        # 초기화
        for a in range(n):
            for b in range(n):
                visited[a][b] = False
                step[a][b] = 0

        for j in candidate:
            hx, hy = hospital[j]

            visited[hx][hy] = True
            queue.append(hospital[j])

        bfs()

        flag = True
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 0:
                    flag = False
                    break

            if not flag:
                break

        if flag:
            max_val = max([
                step[a][b]
                for a in range(n)
                for b in range(n)
            ])

            ans = min(ans, max_val)
        return

    if i == len(hospital):
        if cnt == m:
            # 초기화
            for a in range(n):
                for b in range(n):
                    visited[a][b] = False
                    step[a][b] = 0

            for j in candidate:
                hx, hy = hospital[j]

                visited[hx][hy] = True
                queue.append(hospital[j])

            bfs()

            flag = True
            for i in range(n):
                for j in range(n):
                    if not visited[i][j] and grid[i][j] == 0:
                        flag = False
                        break

                if not flag:
                    break

            if flag:
                max_val = max([
                    step[a][b]
                    for a in range(n)
                    for b in range(n)
                ])

                ans = min(ans, max_val)
        return

    candidate.append(i)
    calculate(i + 1, cnt + 1)
    candidate.pop()

    calculate(i + 1, cnt)

calculate(0, 0)

if ans == int(1e9):
    print(-1)
else:
    print(ans)