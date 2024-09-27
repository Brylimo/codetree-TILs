import sys
sys.setrecursionlimit(100001)

n = int(input())

graph = [[] for _ in range(n + 1)]
step = [0] * (n + 1)
visited = [False] * (n + 1)
for _ in range(n - 1):
    x, y = map(int, input().split())

    graph[x].append(y)
    graph[y].append(x)

def traverse(x):
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            step[i] = step[x] + 1
            traverse(i)


visited[1] = True
traverse(1)

max_idx = -1
max_val = -1
for i in range(1, n + 1):
    if max_val < step[i]:
        max_val = step[i]
        max_idx = i

for i in range(1, n + 1):
    step[i] = 0
    visited[i] = False

visited[max_idx] = True
traverse(max_idx)
step1 = step[:]

max_idx = -1
max_val = -1
for i in range(1, n + 1):
    if max_val < step1[i]:
        max_val = step1[i]
        max_idx = i

for i in range(1, n + 1):
    step[i] = 0
    visited[i] = False

visited[max_idx] = True
traverse(max_idx)
step2 = step[:]

f_step = [0] * (n + 1)
for i in range(1, n + 1):
    f_step[i] = max(step1[i], step2[i])

ans = min(f_step[1:])
print(ans)