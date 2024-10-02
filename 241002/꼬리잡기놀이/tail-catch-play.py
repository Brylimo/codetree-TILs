n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]
tmap = [
    [0] * n
    for _ in range(n)
]
pmap = [
    [-1] * n
    for _ in range(n)
]
path = [[] for _ in range(m + 1)]
dirs = [0] * (m + 1)

score = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

def dfs(x, y, num):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not in_range(nx, ny):
            continue

        if not visited[nx][ny] and grid[nx][ny] > 0:
            visited[nx][ny] = True
            tmap[nx][ny] = num
            pmap[nx][ny] = len(path[num])
            path[num].append(grid[nx][ny])
            dfs(nx, ny, num)

def init():
    num = 1
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] > 0:
                visited[i][j] = True
                tmap[i][j] = num
                pmap[i][j] = 0
                path[num].append(grid[i][j])
                dfs(i, j, num)
                num += 1

    for i in range(1, m + 1):
        idx = path[i].index(3)

        prev = idx - 1
        next = idx + 1

        if prev >= 0 and path[i][prev] == 2:
            dirs[i] = 1
        elif next < len(path[i]) and path[i][next] == 2:
            dirs[i] = 0

def draw():
    for i in range(n):
        for j in range(n):
            if tmap[i][j] > 0:
                team_id = tmap[i][j]
                idx = pmap[i][j]

                grid[i][j] = path[team_id][idx]

def move():
    for i in range(1, m + 1):
        if dirs[i] == 0:
            tmp = path[i].pop()
            path[i] = [tmp] + path[i]
        else:
            tmp = path[i].pop(0)
            path[i].append(tmp)

    draw()

def get_score(team_id, idx):
    global score
    norm_idx = path[team_id].index(1)

    if norm_idx == idx:
        score += 1
    elif dirs[team_id] == 0 and norm_idx > idx:
        score += (norm_idx - idx + 1) ** 2
    elif dirs[team_id] == 0 and norm_idx < idx:
        score += (norm_idx + 1 + len(path[team_id]) - idx) ** 2
    elif dirs[team_id] == 1 and norm_idx < idx:
        score += (idx - norm_idx + 1) ** 2
    else:
        score += (idx + 1 + len(path[team_id]) - norm_idx) ** 2

def throw(r):
    r = r - 1
    round = r % (4 * n)

    if round < n:
        for i in range(n):
            if 1 <= grid[round][i] <= 3:
                team_id = tmap[round][i]
                idx = pmap[round][i]

                get_score(team_id, idx)

                if dirs[team_id] == 1:
                    dirs[team_id] = 0
                else:
                    dirs[team_id] = 1

                one = path[team_id].index(1)
                three = path[team_id].index(3)

                path[team_id][one], path[team_id][three] = path[team_id][three], path[team_id][one]
                break
    elif n <= round < 2 * n:
        round = round % n
        for i in range(n):
            if 1 <= grid[n - i - 1][round] <= 3:
                team_id = tmap[n - i - 1][round]
                idx = pmap[n - i - 1][round]

                get_score(team_id, idx)

                if dirs[team_id] == 1:
                    dirs[team_id] = 0
                else:
                    dirs[team_id] = 1

                one = path[team_id].index(1)
                three = path[team_id].index(3)

                path[team_id][one], path[team_id][three] = path[team_id][three], path[team_id][one]
                break
    elif 2 * n <= round < 3 * n:
        round = round % n
        for i in range(n):
            if 1 <= grid[n - round - 1][n - i - 1] <= 3:
                team_id = tmap[n - round - 1][n - i - 1]
                idx = pmap[n - round - 1][n - i - 1]

                get_score(team_id, idx)

                if dirs[team_id] == 1:
                    dirs[team_id] = 0
                else:
                    dirs[team_id] = 1

                one = path[team_id].index(1)
                three = path[team_id].index(3)

                path[team_id][one], path[team_id][three] = path[team_id][three], path[team_id][one]
                break
    else:
        round = round % n
        for i in range(n):
            if 1 <= grid[i][n - round - 1] <= 3:
                team_id = tmap[i][n - round - 1]
                idx = pmap[i][n - round - 1]

                get_score(team_id, idx)

                if dirs[team_id] == 1:
                    dirs[team_id] = 0
                else:
                    dirs[team_id] = 1

                one = path[team_id].index(1)
                three = path[team_id].index(3)

                path[team_id][one], path[team_id][three] = path[team_id][three], path[team_id][one]
                break

    draw()

init()
for r in range(1, k + 1):
    # 한 칸 이동
    move()

    # 공 던짐
    throw(r)

print(score)