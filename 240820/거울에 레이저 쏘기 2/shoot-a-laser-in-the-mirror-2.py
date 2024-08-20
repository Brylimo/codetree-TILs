n = int(input())
grid = []
for _ in range(n):
    grid.append(list(input()))

k = int(input())

dir = (k - 1) // n
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

seg = (k - 1) % n
if dir == 0:
    x = 0
    y = seg
elif dir == 1:
    y = n - 1
    x = seg
elif dir == 2:
    x = n - 1
    y = n - seg
elif dir == 3:
    y = 0
    x = n - seg

ans = 0
while (0 <= x < n and 0 <= y < n):
    ans += 1
    
    if grid[x][y] == '/':
        if dir % 2 == 0:
            dir = (dir + 1) % 4
        else:
            dir = (dir + 3) % 4
    elif grid[x][y] == '\\':
        if dir % 2 == 0:
            dir = (dir + 3) % 4
        else:
            dir = (dir + 1) % 4

    x = x + dx[dir]
    y = y + dy[dir]

print(ans)