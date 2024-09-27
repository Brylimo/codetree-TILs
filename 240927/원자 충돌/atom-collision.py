n, m, k = map(int, input().split())
atoms = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def init():
    # 초기 원자 배치
    for i in range(len(atoms)):
        x, y, m, s, d = atoms[i]
        grid[x - 1][y - 1].append((m, s, d))

def move():
    global grid

    next_grid = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                length = len(grid[i][j])
                for k in range(length):
                    m, s, d = grid[i][j][k]

                    nx = (i + dx[d] * s) % n
                    ny = (j + dy[d] * s) % n

                    next_grid[nx][ny].append((m, s, d))

    grid = [row for row in next_grid]

def synthesize():
    flask1 = [0, 2, 4, 6]
    flask2 = [1, 3, 5, 7]

    for i in range(n):
        for j in range(n):
            total_m, total_s = 0, 0
            if len(grid[i][j]) >= 2:
                # 하나의 원자로 합치기
                candidates = []
                for t in range(len(grid[i][j])):
                    m, s, d = grid[i][j][t]

                    total_m += m
                    total_s += s

                    candidates.append(d)

                # 방향을 구함
                cnt1, cnt2 = 0, 0
                for dir in candidates:
                    if dir in flask1:
                        cnt1 += 1
                    elif dir in flask2:
                        cnt2 += 1

                new_m = total_m // 5
                new_s = total_s // len(candidates)

                # grid[i][j]에 있던 원소를 모두 뺌
                grid[i][j] = []

                if new_m > 0:
                    if cnt1 == len(candidates) or cnt2 == len(candidates):
                        for dd in flask1:
                            grid[i][j].append((new_m, new_s, dd))
                    else:
                        for dd in flask2:
                            grid[i][j].append((new_m, new_s, dd))

init()
for _ in range(k):
    # 자신의 방향 으로 속력 만큼 이동
    move()

    # 합성 진행
    synthesize()

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            for t in range(len(grid[i][j])):
                ans += grid[i][j][t][0]

print(ans)