import sys
input = sys.stdin.readline

graph = []
n = int(input().rstrip())
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))

visited = [False] * n
answer = []

max_val = 0
def calc(curr_idx):
    global max_val
    if curr_idx == n:
        max_val = max(max_val, sum(answer))        
        return

    for i in range(n):
        if visited[i]:
            continue

        answer.append(graph[curr_idx][i])
        visited[i] = True
        calc(curr_idx + 1)
        visited[i] = False
        answer.pop()

calc(0)
print(max_val)