import sys

n = int(input())
parents = list(map(int, input().split()))
k = int(input())

graph = [[] for _ in range(n)]
visited = [False] * n

root = -1
for i in range(n):
    if parents[i] == -1:
        root = i 
        break

parents[k] = -1
if root == k:
    print(0)
    sys.exit(0)

for i in range(n):
    parent = parents[i]

    if parent == -1:
        continue
    else:
        graph[parents[i]].append(i)

cnt = 0
def traverse(x):
    global cnt 

    if not graph[x]:
        cnt += 1

    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            parents[i] = -1
            traverse(i)

visited[root] = True
traverse(root)

print(cnt)