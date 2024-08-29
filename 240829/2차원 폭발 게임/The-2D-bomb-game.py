n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def rotate():
    # 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0

    # 90도 회전
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[n - j - 1][i]

    # 덮어쓰기
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

def fall():
    # 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0    

    for j in range(n):
        end_of_temp = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j]:
                next_grid[end_of_temp][j] = grid[i][j]
                end_of_temp -= 1

    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

def bomb():
    # 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0

    active = False
    for j in range(n):
        end_of_temp = n - 1
        current, bomb_cnt = None, 0
        for i in range(n - 1, -1, -1):
            if current is None:
                current = grid[i][j]
                bomb_cnt += 1
            elif current == grid[i][j]:
                bomb_cnt += 1
            elif current != grid[i][j]:
                if bomb_cnt >= m:
                    active = True
                    current = grid[i][j]
                else:
                    for k in range(bomb_cnt):
                        next_grid[end_of_temp][j] = current
                        end_of_temp -= 1
                    current = grid[i][j]
                bomb_cnt = 1

        if current:
            if bomb_cnt < m:
                for k in range(bomb_cnt):
                    next_grid[end_of_temp][j] = current
                    end_of_temp -= 1

    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

    return active
def simulate(k):
    for _ in range(k):
        # 폭발
        while bomb():
            pass

        # 90도 회전
        rotate()

        fall()

simulate(k + 1)

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] > 0:
            ans += 1

print(ans)