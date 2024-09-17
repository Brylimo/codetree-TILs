class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

n, q = map(int, input().split())
cities = dict()

array = list(input().split())
pinned = array[0]

for i in array:
    cities[i] = Node(i)

def connect(s, e):
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s

def move_pin_to_right():
    global pinned

    if cities[pinned].next is not None:
        pinned = cities[pinned].next.data

def move_pin_to_left():
    global pinned
    
    if cities[pinned].prev is not None:
        pinned = cities[pinned].prev.data

def pop_right():
    if cities[pinned].next is not None:
        target = cities[pinned].next

        connect(target.prev, target.next)
        target.prev, target.next = None, None

def insert_city(a):
    a.prev = cities[pinned]
    a.next = cities[pinned].next

    connect(a, a.next)
    connect(a.prev, a)

    cities[a.data] = a

for i in range(n - 1):
    connect(cities[array[i]], cities[array[i + 1]])
connect(cities[array[n - 1]], cities[array[0]])

for _ in range(q):
    query = list(input().split())

    option = int(query[0])
    if pinned == None:
        continue

    if option == 1:
        move_pin_to_right()
    elif option == 2:
        move_pin_to_left()
    elif option == 3:
        pop_right()
    elif option == 4:
        a = query[1]
        insert_city(Node(a))

    node = cities[pinned]

    if node is not None:
        if node.prev is not None and node.next is not None and node.prev.data == node.next.data:
            print(-1)
        elif node.prev is None or node.next is None:
            print(-1)
        else:
            if node.prev is not None:
                print(node.prev.data, end=" ")

            if node.next is not None:
                print(node.next.data, end="")

            print()