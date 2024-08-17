import sys
input = sys.stdin.readline

graph  = []
n = int(input().rstrip())
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))

answer = []
visited = [False] * n

min_val = sys.maxsize
def is_possible():
    for tx, ty in answer:
        if (ty, tx) in answer:
            return False

    return True

def calc_sum():
    t_sum = 0
    for tx, ty in answer:
        t_sum += graph[tx][ty]
    return t_sum

def calc(curr_num):
    global min_val
    if curr_num == n:
        if is_possible():
            min_val = min(min_val, calc_sum())
            return
        return

    for i in range(n):
        if visited[i] or curr_num == i or graph[curr_num][i] == 0:
            continue

        answer.append((curr_num, i))
        visited[i] = True
        calc(curr_num + 1)
        visited[i] = False
        answer.pop()

calc(0)
print(min_val)