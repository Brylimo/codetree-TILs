# 한 노드를 나타내는 클래스입니다.
class Node:
    # 번호가 data인 단일 노드를 만드는 생성자
    def __init__(self, id):
        # 책의 번호
        self.id = id

        # 이전 노드와 다음 노드
        self.prev = None
        self.next = None


n, k = map(int, input().split())

# 각 책꽂이의 시작과 끝을 나타내는 변수입니다.
heads = [0] * (k + 1)
tails = [0] * (k + 1)

# 각 노드를 나타내는 변수입니다.
nodes = [None] + [Node(i) for i in range(1, n + 1)]


def empty(line_num):
    # 해당 책꽂이가 비었는지 확인합니다.
    return heads[line_num] == 0


def connect(s, e):
    # 두 노드를 연결해줍니다.
    if s:
        s.next = e
    if e:
        e.prev = s


# line_num 번호의 연결 리스트의 head를 삭제한 후 반환해줍니다.
def pop_front(line_num):
    # 맨 앞의 책을 빼줍니다.
    ret = nodes[heads[line_num]]
    if not ret:
        return None

    if not ret.next:
        heads[line_num] = 0
    else:
        heads[line_num] = ret.next.id

    # 노드 ret를 단일 노드로 만듦
    ret.next = None

    if heads[line_num] != 0:
        # 연결 리스트가 비어있지 않다면, head의 이전 노드를 Null로 설정
        nodes[heads[line_num]].prev = None
    else:
        # 연결 리스트가 비어있다면, tail도 Null로 설정
        tails[line_num] = 0

    return ret


# i번 연결 리스트의 tail을 삭제한 후 반환
def pop_back(line_num):
    ret = nodes[tails[line_num]]
    if not ret:
        return None

    if not ret.prev:
        tails[line_num] = 0
    else:
        tails[line_num] = ret.prev.id

    # 노드 ret를 단일 노드로 만듦
    ret.prev = None

    if tails[line_num] != 0:
        # 연결 리스트가 비어있지 않다면, tail의 다음 노드를 Null로 설정
        nodes[tails[line_num]].next = None
    else:
        # 연결 리스트가 비어있다면, head도 Null로 설정
        heads[line_num] = 0

    return ret


# line_num번 연결 리스트의 맨 앞에 단일 노드 u를 삽입
def push_front(line_num, u):
    # 해당 책꽂이의 맨 앞에 책을 넣어줍니다.
    if heads[line_num] == 0:
        # 연결 리스트가 비어있다면, head와 tail은 모두 u
        tails[line_num] = heads[line_num] = u.id
    else:
        # 연결 리스트가 비어있지 않다면, 기존의 head 앞에 u를 삽입
        connect(u, nodes[heads[line_num]])
        heads[line_num] = u.id


def push_back(line_num, u):
    # 해당 책꽂이의 끝에 책을 넣어줍니다.
    if tails[line_num] == 0:
        # 연결 리스트가 비어있다면, head와 tail은 모두 u
        tails[line_num] = heads[line_num] = u.id
    else:
        # 연결 리스트가 비어있지 않다면, 기존의 tail 뒤에 u를 삽입
        connect(nodes[tails[line_num]], u)
        tails[line_num] = u.id


# i번 책꽂이의 모든 책을 j번 책꽂이로 옮깁니다.
def move_all_front(i, j):
    if i == j or empty(i):
        return

    if empty(j):
        # j번 책꽂이가 비어있다면, i번 책꽂이의 모든 책을 j번 책꽂이로 옮깁니다.
        heads[j] = heads[i]
        tails[j] = tails[i]
    else:
        # j번 연결 리스트가 비어있지 않다면
        # i번의 tail과 j번의 head를 연결하고
        # j번의 head는 i번의 head가 됩니다.
        connect(nodes[tails[i]], nodes[heads[j]])
        heads[j] = heads[i]

    # 이제, i번 연결 리스트는 비어있음
    heads[i] = tails[i] = 0


# i번 연결 리스트를 j번 연결 리스트 뒤에 삽입합니다.
def move_all_back(i, j):
    if i == j or empty(i):
        return

    if empty(j):
        # j번 책꽂이가 비어있다면, i번 책꽂이의 모든 책을 j번 책꽂이로 옮깁니다.
        heads[j] = heads[i]
        tails[j] = tails[i]
    else:
        # j번 연결 리스트가 비어있지 않다면
        # i번의 head와 j번의 tail을 연결하고
        # j번의 tail은 i번의 tail이 됩니다.
        connect(nodes[tails[j]], nodes[heads[i]])
        tails[j] = tails[i]

    # 이제, i번 연결 리스트는 비어있음
    heads[i] = tails[i] = 0


# 1번 책꽂이에 책을 전부 순서대로 꽂습니다.
for i in range(1, n):
    connect(nodes[i], nodes[i + 1])

heads[1] = 1
tails[1] = n

# 쿼리를 처리합니다.
q = int(input())
for _ in range(q):
    option, i, j = map(int, input().split())
    if option == 1:
        target = pop_front(i)
        if target:
            push_back(j, target)
    elif option == 2:
        target = pop_back(i)
        if target:
            push_front(j, target)
    elif option == 3:
        move_all_front(i, j)
    elif option == 4:
        move_all_back(i, j)

# 각 책꽂이의 책을 출력합니다.
for i in range(1, k + 1):
    cnt = 0

    # i번 책꽂이의 책의 개수를 세줍니다.
    cur = nodes[heads[i]]
    while None != cur:
        cnt += 1
        cur = cur.next

    print(cnt, end="")

    # i번 책꽂이의 책의 번호를 출력합니다.
    cur = nodes[heads[i]]
    while None != cur:
        print(f" {cur.id}", end="")
        cur = cur.next
    print()