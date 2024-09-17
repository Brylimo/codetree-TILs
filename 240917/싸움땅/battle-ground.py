n, m, k = map(int, input().split())
grid = [
    [[] for _ in range(n + 1)]
    for _ in range(n + 1)
]

person_x = [0] * (m + 1)
person_y = [0] * (m + 1)
directions = [0] * (m + 1)
energies = [0] * (m + 1)
weapons = [0] * (m + 1)
points = [0] * (m + 1)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def show():
    for i in range(1, n + 1):
        print(grid[i][1:])
    print()

def is_inrange(x, y):
    if 1 <= x <= n and 1 <= y <= n:
        return True

    return False


def move(i):
    x, y = person_x[i], person_y[i]
    dir = directions[i]

    nx = x + dx[dir]
    ny = y + dy[dir]

    if not is_inrange(nx, ny):
        # 방향이 반대로 바뀜
        dir = (dir + 2) % 4
        directions[i] = dir

        nx = x + dx[dir]
        ny = y + dy[dir]

    # 이동
    person_x[i] = nx
    person_y[i] = ny

    for j in range(1, m + 1):
        if j == i:
            continue

        # 이동한 칸에 플레이어가 존재
        if nx == person_x[j] and ny == person_y[j]:
            me = energies[i] + weapons[i]
            oponent = energies[j] + weapons[j]

            winner = None
            loser = None
            if me > oponent:
                winner = i
                loser = j
            elif me < oponent:
                winner = j
                loser = i
            else:
                if energies[i] > energies[j]:
                    winner = i
                    loser = j
                else:
                    winner = j
                    loser = i

            # winner 포인트 획득
            points[winner] += abs(me - oponent)

            # loser 페널티

            # 총을 내려놓음
            if weapons[loser] > 0:
                grid[nx][ny].append(weapons[loser])
                weapons[loser] = 0

            # winner 총 획득
            if len(grid[nx][ny]) > 0:
                fancy_gun = max(grid[nx][ny])

                if fancy_gun > weapons[winner]:
                    grid[nx][ny].remove(fancy_gun)
                    grid[nx][ny].append(weapons[winner])

                    weapons[winner] = fancy_gun

            # loser 한 칸 이동
            loser_x, loser_y = nx, ny
            loser_dir = directions[loser]

            lx = loser_x + dx[loser_dir]
            ly = loser_y + dy[loser_dir]

            while True:
                cant_go = False
                for p in range(1, m + 1):
                    if loser == p:
                        continue

                    # 해당 칸에 다른 플레이어가 있음
                    if lx == person_x[p] and ly == person_y[p]:
                        cant_go = True
                        break

                if not is_inrange(lx, ly) or cant_go:
                    # 90도 회전
                    loser_dir = (loser_dir + 1) % 4

                    # 빈칸 이동
                    lx = loser_x + dx[loser_dir]
                    ly = loser_y + dy[loser_dir]
                else:
                    # 빈칸에 총이 있을 경우
                    if len(grid[lx][ly]) > 0:
                        new_gun = max(grid[lx][ly])

                        grid[lx][ly].remove(new_gun)
                        weapons[loser] = new_gun

                    # 진짜 이동
                    person_x[loser] = lx
                    person_y[loser] = ly
                    directions[loser] = loser_dir

                    break

            return

    # 해당 칸에 플레이어가 존재하지 않음
    if len(grid[nx][ny]) > 0:  # 총이 떨어져 있음
        cool_gun = max(grid[nx][ny])

        if cool_gun > weapons[i]:
            # 주의
            grid[nx][ny].remove(cool_gun)
            if weapons[i] > 0:
                grid[nx][ny].append(weapons[i])

            weapons[i] = cool_gun


for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j, value in enumerate(row, start=1):
        if value > 0:
            grid[i][j].append(value)

# 초기 값 입력
for idx in range(1, m + 1):
    x, y, d, s = map(int, input().split())

    person_x[idx] = x
    person_y[idx] = y
    directions[idx] = d
    energies[idx] = s

for _ in range(k):
    # 플레이어 전체 이동
    for idx in range(1, m + 1):
        move(idx)

    # show()
    '''
    for i in range(1, m + 1):
        print(person_x[i], person_y[i])
    print()
    '''

for i in range(1, m + 1):
    print(points[i], end=" ")