from collections import defaultdict
import heapq, sys

INT_MAX = sys.maxsize

EMPTY = (-1, -1)
q = int(input())
n, m = 0, 0
graph = None

start = 0
dist = None
items = defaultdict(lambda: EMPTY)
queue = []


def construct(elems):
    global n, m, graph, dist

    n, m = elems[0], elems[1]
    dist = [INT_MAX] * n

    graph = [[] for _ in range(n)]
    for i in range(2, len(elems), 3):
        v, u, w = elems[i], elems[i + 1], elems[i + 2]

        graph[v].append((u, w))
        graph[u].append((v, w))


def create_item(elems):
    id, revenue, dest = elems[0], elems[1], elems[2]
    items[id] = (revenue, dest)

    if dist[dest] != INT_MAX and dist[dest] <= revenue:
        heapq.heappush(queue, (-(revenue - dist[dest]), id))

def cancel_item(elems):
    id = elems[0]

    if id in items.keys():
        del items[id]

def dijkstra(x):
    pq = []
    dist[x] = 0
    heapq.heappush(pq, (0, x))

    while pq:
        min_dist, min_idx = heapq.heappop(pq)

        if dist[min_idx] != min_dist:
            continue

        for target_idx, target_dist in graph[min_idx]:
            cost = min_dist + target_dist

            if dist[target_idx] > cost:
                dist[target_idx] = cost
                heapq.heappush(pq, (cost, target_idx))


def sell_item():
    if not queue:
        print(-1)
    else:
        id = -1
        while queue:
            _, id = heapq.heappop(queue)

            if id in items.keys():
                break

        if id in items.keys():
            del items[id]
            print(id)
        else:
            print(-1)

def change_start_point(elems):
    global start, queue

    s = elems[0]
    start = s

    for i in range(n):
        dist[i] = INT_MAX

    dijkstra(start)
    queue = []

    for key, value in items.items():
        if value == EMPTY:
            continue

        rev, dst = value[0], value[1]
        cst = dist[dst]

        if cst != INT_MAX and cst <= rev:
            heapq.heappush(queue, (-(rev - cst), key))


for _ in range(q):
    query = list(map(int, input().split()))

    option = query[0]
    elems = []
    if len(query) > 1:
        elems = query[1:]

    if option == 100:
        construct(elems)
        dijkstra(start)
    elif option == 200:
        create_item(elems)
    elif option == 300:
        cancel_item(elems)
    elif option == 400:
        sell_item()
    elif option == 500:
        change_start_point(elems)