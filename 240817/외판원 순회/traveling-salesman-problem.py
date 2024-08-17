import sys
input = sys.stdin.readline

graph  = []
n = int(input().rstrip())
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))

answer = []
visited = [False] * n

min_val = sys.maxsize
def calc(curr_num):
    global min_val
    if curr_num == n:
        min_val = min(min_val, sum(answer))
        return

    for i in range(n):
        if visited[i] or curr_num == i:
            continue

        answer.append(graph[curr_num][i])
        visited[i] = True
        calc(curr_num + 1)
        visited[i] = False
        answer.pop()

calc(0)
print(min_val)