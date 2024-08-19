import sys
INF = sys.maxsize

n, m = map(int, input().split())

a_array = [INF] * 1000001
b_array = [INF] * 1000001

tick = 0
loc = 0
for i in range(n):
    d, t = input().split()
    t = int(t)

    for j in range(tick + 1, tick + t + 1):
        if d == 'R':
            loc += 1
            a_array[j] = loc
        elif d == 'L':
            loc -= 1
            a_array[j] = loc

    tick += t

tick = 0
loc = 0
for i in range(m):
    d, t = input().split()
    t = int(t)

    for j in range(tick + 1, tick + t + 1):
        if d == 'R':
            loc += 1
            b_array[j] = loc
        elif d == 'L':
            loc -= 1
            b_array[j] = loc

    tick += t

for i in range(1, len(a_array)):
    if a_array[i] == b_array[i] and (a_array[i] != INF or b_array[i] != INF):
        print(i)
        break
    
    if a_array[i] == INF or b_array[i] == INF:
        print(-1)
        break