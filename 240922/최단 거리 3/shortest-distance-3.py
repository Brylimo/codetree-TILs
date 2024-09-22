import sys, heapq
INT_MAX = sys.maxsize

n, m = map(int, input().split())

dist = [INT_MAX] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, s = map(int, input().split())

    graph[x].append((y, s))
    graph[y].append((x, s))

start, end = map(int, input().split())

pq = []
heapq.heappush(pq, (0, start))
dist[start] = 0

while pq:
    min_dist, min_idx = heapq.heappop(pq)

    if min_dist != dist[min_idx]:
        continue

    for target_idx, target_dist in graph[min_idx]:
        cost = dist[min_idx] + target_dist
        if dist[target_idx] > cost:
            dist[target_idx] = cost
            heapq.heappush(pq, (cost, target_idx))

print(dist[end])