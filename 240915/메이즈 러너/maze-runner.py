import heapq

n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

runners = {}

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for idx in range(1, m + 1):
    x, y = map(int, input().split())

    runners[idx] = (x - 1, y - 1)

exit = tuple(map(int, input().split()))
exit = (exit[0] - 1, exit[1] - 1)
moved = [0] * (m + 1)
on_play = [True] * (m + 1)


def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def is_inrange(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    return True


def show_square(square):
    for i in range(len(square)):
        print(square[i])
    print()


def show():
    for i in range(n):
        print(grid[i])
    print()


def move(idx):
    sx, sy = runners[idx]
    ex, ey = exit

    dir = -1
    min_dist = get_dist(sx, sy, ex, ey)
    # 이동 위치 탐색
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]

        if is_inrange(nx, ny) and grid[nx][ny] == 0:
            dist = get_dist(nx, ny, ex, ey)

            if min_dist > dist:
                min_dist = dist
                dir = i

    if dir == -1:  # 움직일 수 없음
        return

    # 최종 움직인 좌표
    ax, ay = sx + dx[dir], sy + dy[dir]
    moved[idx] += 1

    if ax == exit[0] and ay == exit[1]:
        on_play[idx] = False

    runners[idx] = (ax, ay)


def rotate_square(x, y, size):
    global exit
    ex, ey = exit[0], exit[1]

    # 겹치는 위치 확인
    same_loc = [[] for _ in range(m + 1)]

    # 임시 정사각형 생성
    square = [
        [0] * size
        for _ in range(size)
    ]
    next_square = [
        [0] * size
        for _ in range(size)
    ]

    # 벽 정보 삽입
    for i in range(size):
        for j in range(size):
            num = grid[x + i][y + j]
            if num > 0:
                square[i][j] = num - 1

    # 출구 정보 삽입
    square[ex - x][ey - y] = -10

    # 참가자 정보 삽입
    for i in range(1, m + 1):
        rx, ry = runners[i]

        # print("rx, ry", rx, ry)
        if x <= rx < x + size and y <= ry < y + size:
            sx, sy = rx - x, ry - y

            if not square[sx][sy]:
                square[sx][sy] = i + 10
            else:
                # 같은 곳에 참가자가 2명 이상
                iidx = square[sx][sy]
                if iidx > 0:
                    same_loc[iidx - 10].append(i)

    # show_square(square)

    # 정사각형 회전
    for i in range(size):
        for j in range(size):
            next_square[i][j] = square[size - j - 1][i]

    # show_square(next_square)

    # 위치 값 업데이트
    for i in range(size):
        for j in range(size):
            if next_square[i][j] > 10:
                idx = next_square[i][j] - 10
                runners[idx] = (i + x, j + y)

                next_square[i][j] = 0
                while same_loc[idx]:
                    another_idx = same_loc[idx].pop(0)
                    runners[another_idx] = (i + x, j + y)
            elif next_square[i][j] < 0:
                # exit 값 업데이트
                exit = (i + x, j + y)
                next_square[i][j] = 0

            # grid에 값 복사
            grid[x + i][y + j] = next_square[i][j]

def rotate():
    candidates = []
    ex, ey = exit[0], exit[1]

    # 가장 가까운 참가자 찾기
    for idx in range(1, m + 1):
        if not on_play[idx]:
            continue

        x, y = runners[idx]

        w = abs(ey - y)
        h = abs(ex - x)

        nx, ny, side = -1, -1, -1
        if w > h:
            side = w
            ny = min(y, ey)
            nx = max(x, ex) - side

            while nx < 0:
                nx += 1
        else:
            side = h
            ny = max(y, ey) - side
            nx = min(x, ex)

            while ny < 0:
                ny += 1

        heapq.heappush(candidates, (side + 1, nx, ny))

    # 정사각형 정보 획득
    if candidates:
        f_side, f_x, f_y = heapq.heappop(candidates)
        #print(f_x, f_y, f_side)

        # 정사각형 회전
        rotate_square(f_x, f_y, f_side)

        #show()


for _ in range(k):
    cnt = 0

    # 참가자 이동
    for i in range(1, m + 1):
        if on_play[i]:
            move(i)
        else:
            cnt += 1

    if cnt == m:
        break

    # 회전
    rotate()

print(sum(moved))
print(exit[0] + 1, exit[1] + 1)