import sys
from collections import deque
MAX_NUM = 1000000
INF = sys.maxsize

n = int(input())
step = [INF] * (MAX_NUM + 1)
visited = [False] * (MAX_NUM + 1)

def bfs():
    queue = deque()
    queue.append(n)
    visited[n] = True
    step[n] = 0

    while queue:
        num = queue.popleft()

        # 종료 조건
        if num == 1:
            break

        # 1을 뺀다
        if num > 1 and not visited[num - 1]:
            queue.append(num - 1)
            visited[num - 1] = True
            step[num - 1] = min(step[num - 1], step[num] + 1)

        # 1을 더한다
        if num < MAX_NUM and not visited[num + 1]:
            queue.append(num + 1)
            visited[num + 1] = True
            step[num + 1] = min(step[num + 1], step[num] + 1)

        # 2로 나눈다
        if num % 2 == 0 and not visited[num // 2]:
            queue.append(num // 2)
            visited[num // 2] = True
            step[num // 2] = min(step[num // 2], step[num] + 1)

        # 3으로 나눈다
        if num % 3 == 0 and not visited[num // 3]:
            queue.append(num // 3)
            visited[num // 3] = True
            step[num // 3] = min(step[num // 3], step[num] + 1)

bfs()
print(step[1])