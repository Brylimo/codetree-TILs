import sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())
grid = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
visited = [False] * (n + 1)

for i in range(m):
    x, y, s = map(int, input().split())
    grid[x][y] = s

dist = [INT_MAX] * (n + 1)
dist[1] = 0

# 다익스트라 알고리즘
for i in range(1, n + 1):
    min_idx = -1
    for j in range(1, n + 1):
        if visited[j]:
            continue

        if min_idx == -1 or dist[j] < dist[min_idx]:
            min_idx = j

    visited[min_idx] = True

    for j in range(1, n + 1):
        if grid[min_idx][j] == 0:
            continue

        dist[j] = min(dist[j], dist[min_idx] + grid[min_idx][j])

for i in range(2, n + 1):
    if dist[i] == INT_MAX:
        print(-1)
    else:
        print(dist[i])