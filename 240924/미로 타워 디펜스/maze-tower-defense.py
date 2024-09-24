n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
vmap = [
    [0] * n
    for _ in range(n)
]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

monster = []
ans = 0
# 초기화
def init():
    x, y = n // 2, n // 2
    dir = 2
    cnt = 0

    num = 1
    while not (x == 0 and y == 0):
        if dir == 0 or dir == 2:
            cnt += 1

        for i in range(cnt):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if grid[nx][ny] != 0:
                monster.append(grid[nx][ny])

            if nx == 0 and ny == 0:
                x = 0
                y = 0
                vmap[nx][ny] = num
                break

            vmap[nx][ny] = num
            num += 1

            x, y = nx, ny

        dir = (dir + 3) % 4

def tower_attack(d, p):
    global ans

    # 타워 좌표
    x, y = n // 2, n // 2

    candidates = []
    for i in range(1, p + 1):
        nx = x + dx[d] * i
        ny = y + dy[d] * i

        candidates.append(vmap[nx][ny])

    for idx in candidates:
        if idx <= len(monster):
            ans += monster[idx - 1]
            monster.pop(idx - 1)

def monster_disappear():
    global monster, ans

    tlst = [False] * len(monster)
    i = 0
    while True:
        if i >= len(monster) - 1:
            break

        cnt = 1
        for j in range(i + 1, len(monster)):
            if monster[i] == monster[j]:
                cnt += 1
                if j == len(monster) - 1:
                    if cnt >= 4:
                        for k in range(i, j + 1):
                            tlst[k] = True
                        ans += (j + 1 - i) * monster[i]
                    i = j
            else:
                if cnt >= 4:
                    for k in range(i, j):
                        tlst[k] = True
                    ans += (j - i) * monster[i]
                    i = j
                else:
                    i = j
                break

    flag = False
    new_monster = []
    for i in range(len(monster)):
        if not tlst[i]:
            new_monster.append(monster[i])
        else:
            flag = True

    monster = new_monster

    return flag

def monster_grouping():
    global monster

    new_monster = []

    i = 0
    while True:
        cnt = 1
        for j in range(i + 1, len(monster)):
            if monster[i] == monster[j]:
                cnt += 1
                if j == len(monster) - 1:
                    i = j
                    new_monster.append(cnt)
                    new_monster.append(monster[i])
            else:
                new_monster.append(cnt)
                new_monster.append(monster[i])

                if len(new_monster) > n ** 2:
                    break

                i = j
                break

        if i >= len(monster) - 1:
            break

        if len(new_monster) > n ** 2:
            break

    if len(new_monster) <= n ** 2 - 1:
        new_monster.append(cnt)
        new_monster.append(monster[-1])

    monster = new_monster

init()
for _ in range(m):
    d, p = map(int, input().split())

    # tower attack
    tower_attack(d, p)

    # monster disappear
    while True:
        flag = monster_disappear()

        if not flag:
            break

    # monster grouping
    monster_grouping()

print(ans)