n, k = map(int, input().split())
array = list(map(int, input().split()))

grid = [
    [0] * n
    for _ in range(n)
]

time = 0

def end():
    return False

def increase():
    min_val = min(array)

    for i in range(n):
        if array[i] == min_val and array[i] > 0:
            array[i] += 1

def roll():
    dough = [[] for _ in range(n + 1)]

    # 현재 도우를 연결 리스트 형태로 변형
    dough[n] = array

    m = 1
    d_cnt = 1
    # 앞 부분 뜯어내기
    if dough[n - 1]:
        m = len(dough[n - 1])

    temp = [
        [0] * m
        for _ in range(m)
    ]

    for i in range(n, -1, -1):
        for j in range(m):
            temp[idx]


def push():
    pass

def fold():
    pass

while end():
    # 밀가루 1 증가
    increase()

    # 도우를 말다
    roll()

    # 도우를 누른다
    push()

    # 도우를 2번 반으로 접는다
    fold()

    #도우를 누른다
    push()

print("gg")