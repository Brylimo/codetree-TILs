n = int(input())

# n, w, s, e
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

directions = dict()
directions['S'] = 0
directions['E'] = 3
directions['N'] = 2
directions['W'] = 1

nx = 0
ny = 0
for _ in range(n):
    dir, dist = input().split()

    nx = nx + dx[directions[dir]] * int(dist)
    ny = ny + dy[directions[dir]] * int(dist)

print(ny, nx)