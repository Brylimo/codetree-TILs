import sys
sys.setrecursionlimit(10**4 + 1)

n = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
step = [0] * (n + 1)
for _ in range(n - 1):
    a, b, s = map(int, input().split())
    graph[a].append((b, s))
    graph[b].append((a, s))

def traverse(x):
    for i, s in graph[x]:
        if not visited[i]:
            visited[i] = True
            step[i] = step[x] + s
            traverse(i)

step[1] = 0
visited[1] = True
traverse(1)

max_val = -1
nxt_idx = 1
for i in range(1, n + 1):
    if max_val < step[i]:
        max_val = step[i]
        nxt_idx = i

for i in range(1, n + 1):
    visited[i] = False
    step[i] = 0

visited[nxt_idx] = True
traverse(nxt_idx)
print(max(step))