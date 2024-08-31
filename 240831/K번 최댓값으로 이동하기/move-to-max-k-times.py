import sys
from collections import deque

n, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]
r, c = map(int, input().split())
curr_x, curr_y = r - 1, c - 1

def bfs(visited, x, y):
    queue = deque([])
    queue.append((x, y))
    visited[x][y] = True

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    max_val = -1
    while queue:
        ax, ay = queue.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and grid[x][y] > grid[nx][ny]:
                visited[nx][ny] = True
                
                if max_val < grid[nx][ny]:
                    max_val = grid[nx][ny]
                
                queue.append((nx, ny))

    return max_val

for _ in range(k):
    # visited 배열 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    next_val = bfs(visited, curr_x, curr_y)

    if next_val == -1:
        print(curr_x + 1, curr_y + 1)
        sys.exit(0)

    flag = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] and grid[i][j] == next_val:
                curr_x, curr_y = i, j
                flag = True
                break
        if flag:
            break

print(curr_x + 1, curr_y + 1)