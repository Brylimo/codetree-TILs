EMPTY = (-1, -1)
DIR_N = 8
n = 4
m = n * n

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

grid = [
    [EMPTY] * n
    for i in range(n)
]

thief_loc = [EMPTY] * (m + 1)
thief_dir = [0] * (m + 1)
alive = [True] * (m + 1)

for i in range(n):
    given_input = list(map(int, input().split()))
    for j in range(0, len(given_input), 2):
        p = given_input[j]
        d = given_input[j + 1]

        grid[i][j // 2] = (p, d)

        thief_loc[p] = (i, j // 2)
        thief_dir[p] = d

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

def thief_move():
    for i in range(1, m + 1):
        if alive[i]:
            x, y = thief_loc[i]
            dir = thief_dir[i]

            for k in range(DIR_N):
                nx = x + dx[dir]
                ny = y + dy[dir]

                if in_range(nx, ny) and not (nx == tx and ny == ty):
                    # 빈칸
                    if grid[nx][ny] == EMPTY:
                        grid[nx][ny] = (i, dir)
                        grid[x][y] = EMPTY

                    # 다른 도둑말
                    else:
                        op, od = grid[nx][ny]

                        grid[nx][ny] = (i, dir)
                        grid[x][y] = (op, od)

                        thief_loc[op] = (x, y)

                    thief_loc[i] = (nx, ny)
                    break
                else:
                    dir = (dir + 1) % DIR_N
                    thief_dir[i] = dir

def calculate(grid, i):
    nx = tx + dx[tdir] * i
    ny = ty + dy[tdir] * i
    
    if not in_range(nx, ny):
        return
    
    pp = grid[nx][ny][0]
    pdir = grid[nx][ny][1]
    
    alive[pp] = False
    grid[nx][ny] = EMPTY
    
def cop_move():
    flag = True
    for i in range(1, n):
        copied_grid = [arr[:] for arr in grid]
        
        calculate(copied_grid, i)

# 도둑말 등장
tx, ty = 0, 0

score = grid[tx][ty][0]
tdir = grid[tx][ty][1]

alive[score] = False
grid[tx][ty] = EMPTY

# 도둑말 이동
thief_move()

# 술래말 이동
cop_move()