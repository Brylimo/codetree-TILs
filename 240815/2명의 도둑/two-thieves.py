import sys
input = sys.stdin.readline

n, m, c = map(int, input().rstrip().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))

segments = []
def is_durable():
    x1, y1, l1 = segments[0]
    x2, y2, l2 = segments[1]

    sum1 = 0
    for i in range(l1):
        if y1 + i < 0 or y1 + i >= n:
            return False

        sum1 += graph[x1][y1 + i]
    
    sum2 = 0
    for i in range(l2):
        if y2 + i < 0 or y2 + i >= n:
            return False

        sum2 += graph[x2][y2 + i]
    
    if (x1 == x2 and y1 <= y2 < y1 + l1) or (x1 == x2 and y2 <= y1 < y2 + l2) or (x1 == x2 and y1 <= y2 + l2 - 1 < y1 + l1) or (x1 == x2 and y2 <= y1 + l1 - 1 < y2 + l2):
        return False

    if sum1 > c or sum2 > c:
        return False

    return True

answer = 0
def calc(curr_num):
    global answer
    if curr_num == 2:
        if is_durable():
            x1, y1, l1 = segments[0]
            x2, y2, l2 = segments[1]

            value = 0
            for i in range(l1):
                value += (graph[x1][y1 + i] ** 2)

            for i in range(l2):
                value += (graph[x2][y2 + i] ** 2) 

            answer = max(answer, value)
        return

    for i in range(n):
        for j in range(n):
            for k in range(1, m + 1):
                segments.append((i, j, k))
                calc(curr_num + 1)
                segments.pop()

    return

calc(0)
print(answer)