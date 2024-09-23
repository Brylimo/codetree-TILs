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

def insert_range_prev(a, b):
    connect(b.prev, a.next)
    connect(a, b)

def pop_range_prev(a, b):
    temp = b.prev
    connect(a.prev, b)
    connect(temp, a)

n, m, q = map(int, input().split())

student = dict()
for _ in range(m):
    array = list(map(int, input().split()))

    num = array[0]
    for i in range(1, num + 1):
        student[array[i]] = Node(array[i])

    for i in range(1, num):
        connect(student[array[i]], student[array[i + 1]])
    connect(student[array[-1]], student[array[1]])

for _ in range(q):
    query = list(map(int, input().split()))

    option = query[0]
    if option == 1:
        a, b = query[1], query[2]
        insert_range_prev(student[a], student[b])
    elif option == 2:
        a, b = query[1], query[2]
        pop_range_prev(student[a], student[b])
    elif option == 3:
        a = query[1]

        x = student[a]
        min_val = x.data

        while x.next != student[a]:
            x = x.next
            min_val = min(min_val, x.data)

        print(min_val, end=" ")
        x = student[min_val]
        while x.prev != student[min_val]:
            x = x.prev
            print(x.data, end=" ")