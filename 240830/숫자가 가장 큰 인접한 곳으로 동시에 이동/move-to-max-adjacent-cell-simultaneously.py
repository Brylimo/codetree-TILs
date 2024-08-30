n, m, t = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
marbles = [
    tuple(map(int, input().split()))
    for _ in range(m)
]
count = [
    [0 for _ in range(n)]
    for _ in range(n)
]
next_count = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def move(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    max_val = 0
    max_pos = (-1, -1)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if max_val < grid[nx][ny]:
            max_val = grid[nx][ny]
            max_pos = (nx, ny)
            
    next_count[max_pos[0]][max_pos[1]] += 1

def move_all():
    # next_count 초기화
    for i in range(n):
        for j in range(n):
            next_count[i][j] = 0

    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                move(i, j)

    # count에 다시 옮겨주기
    for i in range(n):
        for j in range(n):
            if next_count[i][j] == 1:
                count[i][j] = 1
            else:
                count[i][j] = 0


# count에 구슬 위치를 담음
for mx, my in marbles:
    count[mx - 1][my - 1] = 1

for _ in range(t):
    move_all()

ans = sum([
    count[i][j]
    for i in range(n)
    for j in range(n)
])

print(ans)