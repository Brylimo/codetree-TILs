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

def pop(node):
    connect(node.prev, node.next)
    node.prev = node.next = None

n, m = map(int, input().split())
knights = list(map(int, input().split()))

nodes = dict()
prev = None

for i in range(n):
    nodes[knights[i]] = Node(knights[i])

for i in range(n - 1):
    connect(nodes[knights[i]], nodes[knights[i + 1]])
connect(nodes[knights[-1]], nodes[knights[0]])

# 왕이 기사 번호를 부름
for _ in range(m):
    num = int(input())

    target = nodes[num]
    print(target.next.data, target.prev.data)

    pop(target)