import sys
import heapq
INT_MAX = sys.maxsize

n, m = map(int, input().split())

dist = [INT_MAX] * (n + 1)
path = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, s = map(int, input().split())
    graph[a].append((s, b))
    graph[b].append((s, a))

start, end = map(int, input().split())

def dijkstra(start):
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        min_dist, min_idx = heapq.heappop(pq)

        if dist[min_idx] != min_dist:
            continue

        for d, i in graph[min_idx]:
            if dist[i] > dist[min_idx] + d:
                dist[i] = dist[min_idx] + d 
                path[i] = min_idx
                heapq.heappush(pq, (dist[i], i))

dijkstra(start)

visited = []
visited.append(end)
x = end

while x != start:
    x = path[x]
    visited.append(x)

print(dist[end])
for i in visited[::-1]:
    print(i, end = " ")