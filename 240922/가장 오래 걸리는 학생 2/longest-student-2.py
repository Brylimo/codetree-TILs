import sys
import heapq
INT_MAX = sys.maxsize

n, m = map(int, input().split())
dist = [INT_MAX] * (n + 1)

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j, d = map(int, input().split())
    graph[j].append((i, d))

def dijkstra(n):
    dist[n] = 0
    pq = []

    heapq.heappush(pq, (0, n))

    while pq:
        min_dist, min_idx = heapq.heappop(pq)

        if dist[min_idx] != min_dist:
            continue

        for i, d in graph[min_idx]:
            if dist[i] > dist[min_idx] + d:
                dist[i] = dist[min_idx] + d
                heapq.heappush(pq, (dist[i], i))

dijkstra(n)
print(max(dist[1:]))