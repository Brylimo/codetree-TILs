S_init = input()
n = int(input())

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

cur = Node(S_init)
for _ in range(n):
    inputs = input()

    if inputs.startswith('1'):
        i, v = inputs.split()

        new_node = Node(v)
        new_node.next = cur
        if cur is not None:
            new_node.prev = cur.prev

        if new_node.next is not None:
            new_node.next.prev = new_node
        if new_node.prev is not None:
            new_node.prev.next = new_node
    elif inputs.startswith('2'):
        i, v = inputs.split()

        new_node = Node(v)
        new_node.prev = cur
        if cur is not None:
            new_node.next = cur.next

        if new_node.prev is not None:
            new_node.prev.next = new_node
        if new_node.next is not None:
            new_node.next.prev = new_node
        
    elif inputs.startswith('3'):
        if cur.prev is not None:
            cur = cur.prev
    elif inputs.startswith('4'):
        if cur.next is not None:
            cur = cur.next
    
    if cur is not None and cur.prev is not None:
        print(cur.prev.data, end=" ")
    else:
        print("(Null)", end=" ")

    if cur is not None:
        print(cur.data, end=" ")
    else:
        print("(Null)", end=" ")

    if cur is not None and cur.next is not None:
        print(cur.next.data, end=" ")
    else:
        print("(Null)", end=" ")

    print()