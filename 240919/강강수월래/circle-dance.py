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


def insert_range_next(n, s):
    if s is not None and n is not None:
        connect(s.prev, n.next)
    connect(n, s)


def pop_range_prev(a, b):
    temp = None
    if b is not None:
        temp = b.prev
    if a is not None:
        connect(a.prev, b)
        connect(temp, a)


n, m, q = map(int, input().split())
# 노드를 나타냄
nodes = [None] * (n + 1)

# 초기화
for i in range(m):
    info = list(map(int, input().split()))

    length = info[0]
    for j in range(1, length + 1):
        nodes[info[j]] = Node(info[j])

        if j != 1:
            connect(nodes[info[j - 1]], nodes[info[j]])

    # 원형으로 연결시킴
    connect(nodes[info[-1]], nodes[info[1]])

for _ in range(q):
    query = list(map(int, input().split()))

    option = query[0]
    if option == 1:
        a, b = query[1], query[2]
        insert_range_next(nodes[a], nodes[b])
    elif option == 2:
        a, b = query[1], query[2]
        pop_range_prev(nodes[a], nodes[b])
    elif option == 3:
        a = query[1]

        min_val = int(1e9)
        target = nodes[a]
        while target:
            if min_val > target.data:
                min_val = target.data
            target = target.next
            if target is nodes[a]:
                break

        target = nodes[min_val]
        while target:
            print(target.data, end=" ")
            target = target.prev

            if target is nodes[min_val]:
                break