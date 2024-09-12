from collections import deque

r, c, k = map(int, input().split())

# 골렘의 초기 정보(골렘이 출발하는 열, 골렘의 출구 방향)
golems = [
    tuple(map(int, input().split()))
    for _ in range(k)
]
forest = [
    [0] * c
    for _ in range(r)
]
temp = []

def in_range(x, y):
    if 0 <= x < r and 0 <= y < c:
        return True

    return False

def get_next_golem_down(x, y):
    global temp

    dx = [0, -1, 0, 1, 0]
    dy = [0, 0, 1, 0, -1]

    vtemp = []
    flag = True
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            if i == 2 or i == 4:
                if x >= 0:
                    flag = False
                    break
            continue

        vtemp.append((nx, ny))
        if forest[nx][ny] == 1:
            flag = False
            break

    if flag:
        temp = vtemp
    
    # print("down", flag, x, y, temp)
    return flag

def get_next_golem_left(x, y):    
    dx = [0, -1, 0, 1, 0]
    dy = [-1, -1, 0, -1, -2]

    flag = True
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            if i == 2 or i == 4:
                if x >= 0:
                    flag = False
                    break

            continue

        if forest[nx][ny] == 1:
            flag = False
            break

    # print("left", flag, x, y)    
    return flag

def get_next_golem_right(x, y):
    global temp

    dx = [0, -1, 0, 1, 0]
    dy = [1, 1, 2, 1, 0]

    vtemp = []
    flag = True
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            if i == 2 or i == 4:
                if x >= 0:
                    flag = False
                    break

            continue

        vtemp.append((nx, ny))
        if forest[nx][ny] == 1:
            flag = False
            break
    
    return flag
    
ans = 0
def bfs(x, y, dir):
    global ans
    
    queue = deque()
    visited = [
        [False] * c 
        for _ in range(r)
    ]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]    

    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]

        visited[px][py] = True

    ex, ey = x + dx[dir], y + dy[dir]
    queue.append((ex, ey))
    
    while queue:
        ax, ay = queue.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue

            if not visited[nx][ny] and forest[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))

    for i in range(r - 1, -1, -1):
        for j in range(c):
            if visited[i][j]:
                ans += i + 1
                # print("star", ans)
                return

def move(col, dir):
    global temp

    dir_x = [-1, 0, 1, 0]
    dir_y = [0, 1, 0, -1]

    i = 0
    coll = col
    while True:
        # 아래로 이동
        if get_next_golem_down(i - 1, coll):
            pass
        else:
            if get_next_golem_left(i - 2, coll) and get_next_golem_down(i - 1, coll - 1):
                dir = (dir + 3) % 4
                pass
            elif get_next_golem_right(i - 2, coll) and get_next_golem_down(i - 1, coll + 1):
                dir = (dir + 1) % 4
                pass
            else:
                # 골렘 최종 이동
                for tx, ty in temp:
                    forest[tx][ty] = 1

                if len(temp) < 5:
                    for i in range(r):
                        for j in range(c):
                            forest[i][j] = 0
                    
                    # print()
                    return

                # 골렘 이동
                if len(temp) > 0:
                    bfs(temp[0][0], temp[0][1], dir)
                temp = []
                # show()
                return

        i += 1
        coll = temp[0][1]
        if i == r:
            break

    for tx, ty in temp:
        forest[tx][ty] = 1

    for lx, ly in temp:
        if lx < 0 or lx >= r or ly < 0 or ly >= c:
            for i in range(r):
                for j in range(c):
                    forest[i][j] = 0
            # print()
            return

    # 골렘 이동
    if len(temp) > 0:
        bfs(temp[0][0], temp[0][1], dir)
    temp = []
    # show()

def show():
    for i in range(r):
        print(forest[i])
    print()


for cg, dg in golems:
    move(cg - 1, dg)

print(ans)