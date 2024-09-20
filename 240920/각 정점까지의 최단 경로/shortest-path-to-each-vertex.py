import sys
import heapq
INT_MAX = sys.maxsize

n, m = map(int, input().split())
k = int(input())

graph = [[] for _ in range(n + 1)]
dist = [INT_MAX] * (n + 1)

for _ in range(m):
    x, y, s = map(int, input().split())
    graph[x].append((y, s))
    graph[y].append((x, s))

dist[k] = 0

pq = []
heapq.heappush(pq, (0, k))

while pq:
    min_dist, min_idx = heapq.heappop(pq)

    if min_dist != dist[min_idx]:
        continue

    for i, s in graph[min_idx]:
        if dist[i] > min_dist + s:
            dist[i] = min_dist + s 
            heapq.heappush(pq, (min_dist + s, i))

for i in range(1, n + 1):
    if dist[i] == INT_MAX:
        print(-1)
    else:
        print(dist[i])