import sys, heapq
INT_MAX = sys.maxsize

a, b, n = map(int, input().split())

fees = [0] * (n + 1)
path = [0] * (1001)
dist = [INT_MAX] * (1001)
graph = [[] for _ in range(1001)]
first_bus = []
for i in range(1, n + 1):
    fee, slen = map(int, input().split())
    stations = list(map(int, input().split()))

    fees[i] = fee
    for j in range(slen - 1):
        if stations[j] == a:
            first_bus.append(i)

        graph[stations[j]].append((stations[j + 1], i))

pq = []
for k in range(len(first_bus)):
    heapq.heappush(pq, (fees[first_bus[k]], a, first_bus[k]))
    dist[a] = min(dist[a], fees[first_bus[k]])

while pq:
    min_dist, min_idx, bb = heapq.heappop(pq)

    if min_idx != a and min_dist != dist[min_idx]:
        continue

    for target_idx, bus_num in graph[min_idx]:
        cost = INT_MAX
        if bb != bus_num:
            if min_idx == a:
                cost = fees[bb] + fees[bus_num]
            else:
                cost = dist[min_idx] + fees[bus_num]
        else:
            if min_idx == a:
                cost = fees[bb]
            else:
                cost = dist[min_idx]

        if dist[target_idx] > cost:
            dist[target_idx] = cost
            path[target_idx] = min_idx
            heapq.heappush(pq, (cost, target_idx, bus_num))

if dist[b] == INT_MAX:
    print(-1, -1)
else:
    x = b
    cnt = 1
    while x != a:
        cnt += 1
        x = path[x]

    print(dist[b], cnt - 1)