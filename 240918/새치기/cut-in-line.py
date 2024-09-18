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

def pop(s):
    for i in range(1, m + 1):
        if lines[i] is not None and lines[i] == s:
            lines[i] = None
            break

    connect(s.prev, s.next)
    s.prev = s.next = None

def insert_prev(n, s):
    for i in range(1, m + 1):
        if lines[i] is not None and lines[i] == n:
            lines[i] = s
            break

    connect(n.prev, s)
    connect(s, n)

def pop_range_insert_prev(a, b, c):
    for i in range(1, m + 1):
        if lines[i] is not None and lines[i] == c:
            lines[i] = a
            break
    
    connect(a.prev, b.next)
    a.prev = b.next = None

    connect(c.prev, a)
    connect(b, c)

n, m, q = map(int, input().split())

# 줄의 수
lines = [None] * (m + 1)
nodes = [None] * (n + 1)

# 초기화
for i in range(1, n + 1):
    nodes[i] = Node(i)

for i in range(1, m + 1):
    line = list(map(int, input().split()))

    line_size = line[0]

    # 해당 줄에 사람이 없음
    if line_size == -1:
        continue

    # 줄의 가장 앞에 있는 사람 등록
    lines[i] = nodes[line[1]]
    for j in range(1, line_size):
        connect(nodes[line[j]], nodes[line[j + 1]])

for i in range(q):
    query = list(map(int, input().split()))
    option = query[0]

    if option == 1:
        pop(nodes[query[1]])
        insert_prev(nodes[query[2]], nodes[query[1]])
    elif option == 2:
        pop(nodes[query[1]])
    elif option == 3:
        pop_range_insert_prev(nodes[query[1]], nodes[query[2]], nodes[query[3]])

for i in range(1, m + 1):
    if lines[i] == None:
        print(-1)
    else:
        target = lines[i]

        while target:
            print(target.data, end=" ")

            target = target.next
        print()