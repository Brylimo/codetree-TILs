import sys
sys.setrecursionlimit(10 ** 5)

n = int(input())
graph = [[] for _ in range(n + 1)]

d = [[0] * (n + 1) for _ in range(n + 1)]
parents = [-1] * (n + 1)
visited = [False] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            parents[i] = x
            dfs(i)

    d[x][0] = 0
    d[x][1] = 1
    for i in graph[x]:
        if parents[i] == x:
            d[x][0] += d[i][1]
            d[x][1] += d[i][0]

visited[1] = True
dfs(1)

print(min(d[1][0], d[1][1]))