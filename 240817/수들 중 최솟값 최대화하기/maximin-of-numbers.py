import sys
input = sys.stdin.readline

n = int(input().rstrip())
cost = [
    list(map(int, input().rstrip().split()))
    for _ in range(n)
]

visited = [False] * n
answer = []

max_val = 0
def calc(curr_idx):
    global max_val
    if curr_idx == n:
        max_val = max(max_val, min(answer))
        return

    for i in range(n):
        if visited[i]:
            continue

        answer.append(cost[curr_idx][i])
        visited[i] = True
        calc(curr_idx + 1)
        visited[i] = False
        answer.pop()

calc(0)
print(max_val)