n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
step = [0] * (n + 1)
for _ in range(n - 1):
    x, y, s = map(int, input().split())
    graph[x].append((y, s))
    graph[y].append((x, s))

def traverse(x, y):
    for i, s in graph[x]:
        if not visited[i]:
            visited[i] = True
            step[i] = step[x] + s
            traverse(i, s)

for i in range(m):
    x, y = map(int, input().split())

    for j in range(n + 1):
        step[j] = 0
        visited[j] = False

    ans = 0
    visited[x] = True
    traverse(x, y)

    ans += step[y]

    print(ans)