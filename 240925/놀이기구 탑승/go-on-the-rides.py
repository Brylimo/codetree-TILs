n = int(input())

grid = [
    [0] * n
    for _ in range(n)
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

score = [0, 1, 10, 100, 1000]
orders = []
vmap = [[] for _ in range(n ** 2 + 1)]
for _ in range(n * n):
    n0, n1, n2, n3, n4 = map(int, input().split())

    orders.append(n0)
    array = [n1, n2, n3, n4]
    vmap[n0][:] = array[:]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

def dispatch(x):

    # 위치 선정
    slst = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:

                like_cnt = 0
                void_cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if not in_range(nx, ny):
                        continue

                    if grid[nx][ny] != 0 and grid[nx][ny] in vmap[x]:
                        like_cnt += 1
                    elif grid[nx][ny] == 0:
                        void_cnt += 1

                slst.append((-like_cnt, -void_cnt, i, j))

    slst.sort()

    # 최적의 위치를 고름
    like_cnt, void_cnt, i, j = slst[0]

    grid[i][j] = x

ans = 0
def calculate():
    global ans

    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                x = grid[i][j]

                like_cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if not in_range(nx, ny):
                        continue

                    if grid[nx][ny] in vmap[x]:
                        like_cnt += 1

                ans += score[like_cnt]

for x in orders:
    dispatch(x)

calculate()
print(ans)