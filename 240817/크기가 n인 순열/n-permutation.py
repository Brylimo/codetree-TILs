n = int(input())

answer = []
visited = [False] * n
def calc(curr_num):
    if curr_num == n + 1:
        for k in answer:
            print(k, end=" ")
        print()
        return

    for i in range(1, n+1):
        if visited[i - 1]:
            continue

        answer.append(i)
        visited[i - 1] = True
        calc(curr_num + 1)
        visited[i - 1] = False
        answer.pop()

    return

calc(1)