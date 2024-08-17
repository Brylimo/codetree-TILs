n = int(input())

visited= [False] * (n + 1)
answer = []
def calc(curr_num):
    if curr_num == n + 1:
        for k in answer:
            print(k, end=" ")
        print()
        return

    for i in range(n, 0, -1):
        if visited[i]:
            continue

        answer.append(i)
        visited[i] = True
        calc(curr_num + 1)
        visited[i] = False
        answer.pop()

calc(1)