class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

n = int(input())
q = int(input())

ids = [None] * (n + 1)

for i in range(1, n + 1):
    ids[i] = Node(i)

def insert_prev(node, singleton):
    singleton.next = node
    singleton.prev = node.prev

    if singleton.prev is not None:
        singleton.prev.next = singleton
    if singleton.next is not None:
        singleton.next.prev = singleton

def insert_next(node, singleton):
    singleton.prev = node
    singleton.next = node.next

    if singleton.prev is not None:
        singleton.prev.next = singleton
    if singleton.next is not None:
        singleton.next.prev = singleton

for _ in range(q):
    inputs = input()

    if inputs.startswith('1'):
        option, i = map(int, inputs.split())

        if ids[i].prev is not None:
            ids[i].prev.next = ids[i].next

        if ids[i].next is not None:
            ids[i].next.prev = ids[i].prev

        ids[i].prev = None
        ids[i].next = None
    elif inputs.startswith('2'):
        option, i, j = map(int, inputs.split())

        insert_prev(ids[i], ids[j])
    elif inputs.startswith('3'):
        option, i, j = map(int, inputs.split())

        insert_next(ids[i], ids[j])
    elif inputs.startswith('4'):
        option, i = map(int, inputs.split())

        target = ids[i]
        if target.prev is not None:
            print(target.prev.data, end=" ")
        else:
            print(0, end=" ")

        if target.next is not None:
            print(target.next.data, end=" ")
        else:
            print(0, end=" ")

        print()


for i in range(1, n + 1):
    if ids[i].next is not None:
        print(ids[i].next.data, end=" ")
    else:
        print(0, end=" ")