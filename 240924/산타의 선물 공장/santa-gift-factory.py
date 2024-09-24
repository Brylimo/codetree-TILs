class Node:
    def __init__(self, id, w):
        self.id = id
        self.w = w
        self.prev = None
        self.next = None

def connect(s, e):
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s

def pop(x):
    for i in range(m):
        if heads[i] == x:
            heads[i] = x.next
        if tails[i] == x:
            tails[i] = x.prev

    connect(x.prev, x.next)
    x.prev = x.next = None

def insert_back(n, s):
    for i in range(m):
        if tails[i] == n:
            tails[i] = s

    connect(s, n.next)
    connect(n, s)

heads = [None] * 11
tails = [None] * 11

def get_belt_num(n):
    x = n
    while x.prev is not None:
        x = x.prev

    num = -1
    for i in range(m):
        if heads[i] is x:
            num = i
            break

    return num

def pop_range_insert_prev(a, b, n):
    for i in range(m):
        if heads[i] == a:
            heads[i] = b.next
        if tails[i] == b:
            tails[i] = a.prev

    connect(a.prev, b.next)
    a.prev = b.next = None

    for i in range(m):
        if heads[i] == n:
            heads[i] = a

    connect(b, n)

def pop_range_insert_next(a, b, n):
    for i in range(m):
        if heads[i] == a:
            heads[i] = b.next
        if tails[i] == b:
            tails[i] = a.prev

    connect(a.prev, b.next)
    a.prev = b.next = None

    for i in range(m):
        if tails[i] == n:
            tails[i] = b

    connect(n, a)

def search_ok_belt(id):
    for i in range(id + 1, m):
        if not outs[i]:
            return i

    for i in range(id):
        if not outs[i]:
            return i

n, m = 0, 0

nodes = dict()
outs = [False] * 11

q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))

    option = query[0]
    if option == 100:
        n, m = query[1], query[2]

        size = n // m

        ids = query[3:3+n]
        weights = query[3+n:3+2*n]

        for i in range(n):
            nodes[ids[i]] = Node(ids[i], weights[i])

            cont_idx = i // size

            if heads[cont_idx] is None:
                heads[cont_idx] = tails[cont_idx] = nodes[ids[i]]
            else:
                connect(tails[cont_idx], nodes[ids[i]])
                tails[cont_idx] = nodes[ids[i]]

    elif option == 200:
        w_max = query[1]

        ans = 0
        for i in range(m):
            if heads[i] is not None:
                target = heads[i].w

                if target <= w_max:
                    ans += target
                    del nodes[heads[i].id]
                    # 하차
                    pop(heads[i])
                else:
                    # 벨트 맨 뒤
                    node = heads[i]
                    pop(node)
                    insert_back(tails[i], node)
        print(ans)
    elif option == 300:
        r_id = query[1]

        target = None
        if r_id in nodes.keys():
            target = nodes[r_id]

        if target is None:
            print(-1)
        else:
            del nodes[r_id]
            pop(target)
            print(r_id)
    elif option == 400:
        f_id = query[1]

        target = None
        if f_id in nodes.keys():
            target = nodes[f_id]

        if target is None:
            print(-1)
        else:
            b_num = get_belt_num(target)
            pop_range_insert_prev(target, tails[b_num], heads[b_num])

            print(b_num + 1)
    elif option == 500:
        b_num = query[1]
        b_num -= 1

        if outs[b_num]:
            print(-1)
        else:
            outs[b_num] = True
            bid = search_ok_belt(b_num)

            pop_range_insert_next(heads[b_num], tails[b_num], tails[bid])
            print(b_num + 1)