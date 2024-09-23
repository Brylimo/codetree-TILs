import math

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

def insert_prev(a, b):
    for i in range(1, m + 1):
        if lines_head[i] == a:
            lines_head[i] = a.next

    connect(a.prev, a.next)
    a.prev = a.next = None

    for i in range(1, m + 1):
        if lines_head[i] == b:
            lines_head[i] = a

    connect(b.prev, a)
    connect(a, b)

def insert_range_prev(a, b, c):
    for i in range(1, m + 1):
        if lines_head[i] == a:
            lines_head[i] = b.next

    connect(a.prev, b.next)
    a.prev = b.next = None

    for i in range(1, m + 1):
        if lines_head[i] == c:
            lines_head[i] = a

    connect(c.prev, a)
    connect(b, c)
def pop(a):
    for i in range(1, m + 1):
        if lines_head[i] == a:
            lines_head[i] = a.next

    connect(a.prev, a.next)
    a.prev = a.next = None

n, m, q = map(int, input().split())
x = n // m

lines_head = [None] * (m + 1)
lines_tail = [None] * (m + 1)

person = dict()
array = list(input().split())
for idx, p in enumerate(array, start = 1):
    line_idx = math.ceil(idx / x)
    inline_idx = ((idx - 1) % x) + 1

    person[array[idx - 1]] = Node(array[idx - 1])
    if lines_head[line_idx] is None:
        lines_head[line_idx] = lines_tail[line_idx] = person[array[idx - 1]]
    else:
        connect(lines_tail[line_idx], person[array[idx - 1]])
        lines_tail[line_idx] = lines_tail[line_idx].next

for _ in range(q):
    query = list(input().split())

    option = int(query[0])
    if option == 1:
        a, b = query[1], query[2]
        insert_prev(person[a], person[b])
    elif option == 2:
        a = query[1]
        pop(person[a])
    elif option == 3:
        a, b, c = query[1], query[2], query[3]
        insert_range_prev(person[a], person[b], person[c])

for i in range(1, m + 1):
    if lines_head[i] is None:
        print(-1)
    else:
        x = lines_head[i]

        print(x.data, end=" ")
        while x.next is not None:
            x = x.next
            print(x.data, end=" ")

        print()