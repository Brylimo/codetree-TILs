import sys
from collections import deque

n, h, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
step = [
    [0] * n
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]
distance = [
    [0] * n
    for _ in range(n)
]

def bfs(x, y):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        ax, ay = queue.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and grid[nx][ny] != 1:
                visited[nx][ny] = True
                step[nx][ny] = step[ax][ay] + 1
                queue.append((nx, ny))

def show():
    for i in range(n):
        print(step[i])
    print()

def get_distance(x, y):
    # visited, step 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0

    bfs(x, y)

    min_val = sys.maxsize
    for sx, sy in shelters:
        if visited[sx][sy]: 
            min_val = min(min_val, step[sx][sy])

    if min_val != sys.maxsize:
        distance[x][y] = min_val
    else:
        distance[x][y] = -1

shelters = []
people = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 3:
            shelters.append((i, j))
        elif grid[i][j] == 2:
            people.append((i, j))

for x, y in people:
    get_distance(x, y)

for i in range(n):
    for j in range(n):
        print(distance[i][j], end=" ")
    print()