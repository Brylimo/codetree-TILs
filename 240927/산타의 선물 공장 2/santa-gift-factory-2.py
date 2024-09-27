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

def pop_range_and_prev(a, b, c, flag, cnt):
    la = lines[a.data]
    lc = lines[c.data]

    if flag:
        counts[lc] += cnt
        counts[la] -= cnt
    else:
        counts[lc] += counts[la]
        counts[la] = 0

    if head[la] is a:
        head[la] = b.next
    if tail[la] is b:
        tail[la] = a.prev

    connect(a.prev, b.next)
    a.prev = b.next = None

    if head[lc] == c:
        head[lc] = a

    connect(b, c)

    x = a
    lines[x.data] = lc
    while x is not b:
        x = x.next
        lines[x.data] = lc

def pop_range_half_and_prev(a, c, m_dst):
    la = lines[a.data]

    b = None
    x = a
    cnt = 0
    while True:
        cnt += 1
        if cnt == counts[la] // 2:
            b = x
            break

        x = x.next

    if c is not None:
        pop_range_and_prev(a, b, c, True, cnt)
    else:
        a.prev = b.next = None

        head[m_dst] = a
        tail[m_dst] = b
        counts[m_dst] = cnt

        x = a
        lines[x.data] = m_dst
        while x is not b:
            x = x.next
            lines[x.data] = m_dst

def pop(s):
    ls = lines[s.data]

    counts[ls] -= 1

    if head[ls] is s:
        head[ls] = s.next
    if tail[ls] is s:
        tail[ls] = s.prev

    connect(s.prev, s.next)
    s.prev = s.next = None

    return s

def append_prev(n, s):
    ln = lines[n.data]

    counts[ln] += 1

    if head[ln] is n:
        head[ln] = s

    connect(n.prev, s)
    connect(s, n)

    lines[s.data] = ln

q = int(input())
n, m = -1, -1

head = []
tail = []
counts = []
nodes = []
lines = []

for _ in range(q):
    query = list(map(int, input().split()))

    option = query[0]

    if option == 100:
        n, m = query[1], query[2]

        # 벨트의 head와 tail 관리
        head = [None] * (n + 1)
        tail = [None] * (n + 1)
        counts = [0] * (n + 1)

        # 노드 관리
        nodes = [None] * (m + 1)
        lines = [0] * (m + 1)

        for i, idx in enumerate(query[3:], start = 1):
            nodes[i] = Node(i)
            lines[i] = idx
            counts[idx] += 1

            if head[idx] is None:
                head[idx] = nodes[i]
                tail[idx] = nodes[i]
            else:
                connect(tail[idx], nodes[i])
                tail[idx] = nodes[i]

    elif option == 200:
        m_src, m_dst = query[1], query[2]
        pop_range_and_prev(head[m_src], tail[m_src], head[m_dst], False, 0)

        print(counts[m_dst])
    elif option == 300:
        m_src, m_dst = query[1], query[2]

        sn, dn = None, None
        if head[m_src] is not None:
            sn = pop(head[m_src])
        if head[m_dst] is not None:
            dn = pop(head[m_dst])

        if sn is not None:
            if head[m_dst] is not None:
                append_prev(head[m_dst], sn)
            else:
                head[m_dst] = sn
                tail[m_dst] = sn
                counts[m_dst] = 1
                lines[sn.data] = m_dst
        if dn is not None:
            if head[m_src] is not None:
                append_prev(head[m_src], dn)
            else:
                head[m_src] = dn
                tail[m_src] = dn
                counts[m_src] = 1
                lines[dn.data] = m_src

        print(counts[m_dst])
    elif option == 400:
        m_src, m_dst = query[1], query[2]

        if counts[m_src] > 1:
            pop_range_half_and_prev(head[m_src], head[m_dst], m_dst)

        print(counts[m_dst])
    elif option == 500:
        p_num = query[1]

        p_node = nodes[p_num].prev
        n_node = nodes[p_num].next

        pp, nn = -1, -1
        if p_node is not None:
            pp = p_node.data
        if n_node is not None:
            nn = n_node.data

        print(pp + 2 * nn)
    elif option == 600:
        b_num = query[1]

        a, b, c = -1, -1, 0
        if head[b_num] is not None:
            a = head[b_num].data
        if tail[b_num] is not None:
            b = tail[b_num].data

        c = counts[b_num]

        print(a + 2 * b + 3 * c)