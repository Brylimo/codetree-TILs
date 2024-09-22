import heapq, sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
dist = [INT_MAX] * (n + 1)
path = [0] * (n + 1)

for _ in range(m):
    x, y, s = map(int, input().split())
    graph[x].append((y, s))
    graph[y].append((x, s))

start, end = map(int, input().split())

pq = []
heapq.heappush(pq, (0, end))
dist[end] = 0

while pq:
    min_dist, min_idx = heapq.heappop(pq)

    if min_dist != dist[min_idx]:
        continue

    for target_idx, target_dist in graph[min_idx]:
        cost = dist[min_idx] + target_dist

        if dist[target_idx] > cost:
            dist[target_idx] = cost
            path = min_idx
            heapq.heappush(pq, (cost, target_idx))

# 최단 거리
print(dist[start])

x = start
print(x, end=" ")
while x != end:
    for i in range(1, n + 1):
        temp = -1
        for a, b in graph[i]:
            if a == x:
                temp = b

        if temp == -1:
            continue

        if dist[i] + temp == dist[x]:
            x = i 
            break

    print(i, end=" ")