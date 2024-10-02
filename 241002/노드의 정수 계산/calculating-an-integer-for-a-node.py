import sys
sys.setrecursionlimit(10 ** 5)

n = int(input())

parents = [-1] * (n + 1)
visited = [False] * (n + 1)

d = [0] * (n + 1)
array = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    t, a, p = map(int, input().split())

    if t == 1:
        array[i] = a
    else:
        array[i] = -a

    parents[i] = p
    graph[i].append(p)
    graph[p].append(i)

def dfs(x):
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

    d[x] = array[x]
    for i in graph[x]:
        if parents[i] == x:
            if d[i] > 0:
                d[x] += d[i]

visited[1] = True
dfs(1)

print(d[1])