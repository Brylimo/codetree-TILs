import sys
from collections import deque

INF = sys.maxsize

n, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [[False] * 4 for _ in range(n)]
    for _ in range(n)
]
step = [
    [INF] * n 
    for _ in range(n)
]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
r1, r2, c1, c2 = r1 - 1, r2 - 1, c1 - 1, c2 - 1

queue = deque()

def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y, dir, power = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny][dir]:
                if grid[nx][ny] == 1 and power > 0:
                    step[nx][ny] = min(step[nx][ny], step[x][y] + 1)
                    visited[nx][ny][dir] = True
                    queue.append((nx, ny , dir, power - 1))
                elif grid[nx][ny] == 0:
                    step[nx][ny] = min(step[nx][ny], step[x][y] + 1)
                    visited[nx][ny][dir] = True
                    queue.append((nx, ny , dir, power))

step[r1][c1] = 0
queue.append((r1, c1, 1, k))
queue.append((r1, c1, 2, k))

def show():
    for i in range(n):
        print(step[i])
    print()

# 4 방향 모두 방문 처리
for i in range(4):
    visited[r1][c1][i] = True

bfs()

if step[r2][c2] == INF:
    print(-1)
else:
    print(step[r2][c2])