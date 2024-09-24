n = int(input())
graph = [
    [] for _ in range(n + 1)
]

visited = [0] * (n + 1)
parent = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def traverse(x):
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            parent[i] = x
            traverse(i)

visited[1] = True
traverse(1)

for i in range(2, n + 1):
    print(parent[i])