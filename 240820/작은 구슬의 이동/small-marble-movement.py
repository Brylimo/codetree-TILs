n, t = map(int, input().split())
r, c, d = input().split()

grid = [[0] * n for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

mapper = {
    'U': 0,
    'R': 1,
    'D': 3,
    'L': 2
}

dir = mapper[d]
x,y = int(r) - 1, int(c) - 1
for i in range(t):
    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        dir = 3 - dir 
    else:
        x = nx
        y = ny

print(x + 1, y + 1)