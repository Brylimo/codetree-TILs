n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
def dfs(vertex):
    global cnt

    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            cnt += 1
            visited[curr_v] = True
            dfs(curr_v)

visited[1] = True
dfs(1)

print(cnt)