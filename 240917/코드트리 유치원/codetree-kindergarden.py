class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def connect(s, e):
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s

def line_next_a(a, b):
    global idx
    idx += 1

    start_idx = idx
    end_idx = idx + b - 1

    for i in range(idx, idx + b):
        nodes[i] = Node(i)

    for i in range(idx, idx + b - 1):
        connect(nodes[i], nodes[i + 1])

    connect(nodes[end_idx], nodes[a].next)
    connect(nodes[a], nodes[start_idx])
    idx = end_idx

def line_prev_a(a, b):
    global idx
    idx += 1

    start_idx = idx
    end_idx = idx + b - 1

    for i in range(idx, idx + b):
        nodes[i] = Node(i)

    for i in range(idx, idx + b - 1):
        connect(nodes[i], nodes[i + 1])

    connect(nodes[a].prev, nodes[start_idx])
    connect(nodes[end_idx], nodes[a])
    idx = end_idx

nodes = dict()
nodes[1] = Node(1)
idx = 1

q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))

    option = query[0]
    if option == 1:
        a, b = query[1], query[2]
        line_next_a(a, b)
    elif option == 2:
        a, b = query[1], query[2]
        line_prev_a(a, b)
    elif option == 3:
        a = query[1]

        target = nodes[a]
        if target.prev is None or target.next is None:
            print(-1)
        else:
            print(target.prev.data, end=" ")
            print(target.next.data)