import sys, heapq
INT_MAX = sys.maxsize

n, m = map(int, input().split())
a, b, c = map(int, input().split())
graph = [
    [] for _ in range(n + 1)
]

dist = [INT_MAX] * (n + 1)
for _ in range(m):
    i, j, s = map(int, input().split())
    graph[i].append((j, s))
    graph[j].append((i, s))

pq = []
dist[a] = 0
dist[b] = 0
dist[c] = 0

heapq.heappush(pq, (0, a))
heapq.heappush(pq, (0, b))
heapq.heappush(pq, (0, c))

while pq:
    min_dist, min_idx = heapq.heappop(pq)

    if min_dist != dist[min_idx]:
        continue

    for target_idx, target_dist in graph[min_idx]:
        cost = dist[min_idx] + target_dist

        if dist[target_idx] > cost:
            dist[target_idx] = cost
            heapq.heappush(pq, (cost, target_idx))

print(max([
    dist[i]
    for i in range(1, n + 1)
    if dist[i] != INT_MAX
]))