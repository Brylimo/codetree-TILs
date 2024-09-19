n, m, k, c = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0] * n
    for _ in range(n)
]
herbicides = [
    [0] * n
    for _ in range(n)
]

ans = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    return True

def grow():
    for i in range(n):
        for j in range(n):

            if grid[i][j] > 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if in_range(nx, ny) and grid[nx][ny] > 0:
                        grid[nx][ny] += 1

def spread():
    # 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[i][j]

    for i in range(n):
        for j in range(n):
            if grid[i][j] <= 0:
                continue

            cnt = 0
            candidates = []
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if not in_range(nx, ny):
                    continue

                if grid[nx][ny] == 0 and herbicides[nx][ny] == 0:
                    cnt += 1
                    candidates.append((nx, ny))

            num = 0
            if cnt > 0:
                num = grid[i][j] // cnt

            for k in range(len(candidates)):
                ax, ay = candidates[k]

                next_grid[ax][ay] += num

    # 옮기기
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

def remove():
    global ans

    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]

    max_cnt = 0
    cx, cy = 0, 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] <= 0:
                continue

            # 현재 칸에 있는 개수
            cnt = grid[i][j]

            flag = [False] * 4
            # 제초제 영향력 찾기
            for e in range(1, k + 1):

                for t in range(4):
                    if flag[t]:
                        continue

                    nx = i + dx[t] * e
                    ny = j + dy[t] * e

                    if not in_range(nx, ny):
                        continue

                    # 나무가 있는 경우
                    if grid[nx][ny] > 0:
                        cnt += grid[nx][ny]
                    else:
                        flag[t] = True

            if max_cnt < cnt:
                max_cnt = cnt
                cx, cy = i, j

    ans += max_cnt
    # 실제 제초제 뿌리기
    grid[cx][cy] = 0
    herbicides[cx][cy] = c
    flag = [False] * 4
    for e in range(1, k + 1):
        for t in range(4):
            if flag[t]:
                continue

            nx = cx + dx[t] * e
            ny = cy + dy[t] * e

            if not in_range(nx, ny):
                continue

            # 나무가 있는 경우
            if grid[nx][ny] > 0:
                grid[nx][ny] = 0
                herbicides[nx][ny] = c
            elif grid[nx][ny] <= 0:
                herbicides[nx][ny] = c
                flag[t] = True

for _ in range(m):
    # 성장
    grow()

    # 번식
    spread()

    # 제초제 수명 깍임
    for i in range(n):
        for j in range(n):
            if herbicides[i][j] > 0:
                herbicides[i][j] -= 1

    # 제초제 박멸
    remove()

print(ans)