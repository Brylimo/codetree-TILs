n = int(input())

root = 1
graph = [[] for _ in range(n + 1)]
parent = [-1] * (n + 1)
visited = [False] * (n + 1)
piece = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
def traverse(x):
    global cnt

    is_leaf = True

    for i in graph[x]:
        if not visited[i]:
            visited[i] = True

            parent[i] = x
            traverse(i)
            is_leaf = False

    if is_leaf:
        piece[x].append(cnt)
        cnt += 1

visited[root] = True
traverse(root)

flag = 1
while True:
    moved = False

    for i in range(1, n + 1):
        if piece[i]: # 장기말이 있다면
            p = piece[i].pop()
            piece[parent[i]].append(p)
            flag += 1
            moved = True
            break

    if piece[root]:
        for k in range(len(piece[root])):
            piece[root].pop()

    if not moved:
        break

if flag % 2 == 0:
    print(1)
else:
    print(0)