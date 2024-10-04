import sys
sys.setrecursionlimit(10 ** 5)

n, r, q = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parents = [0] * (n + 1)
d = [0] * (n + 1)

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

    d[x] = 1
    for i in graph[x]:
        if parents[i] == x:
            d[x] += d[i]

visited[r] = True
dfs(r)
for _ in range(q):
    u = int(input())

    print(d[u])