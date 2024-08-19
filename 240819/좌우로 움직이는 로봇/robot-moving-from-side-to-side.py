n, m = map(int, input().split())

pos_n = [0] * 1000001
tick = 1
for _ in range(n):
    t, d = input().split()
    t = int(t)

    if d == 'L':
        for i in range(t):
            pos_n[tick] = pos_n[tick - 1] - 1
            tick += 1
    elif d == 'R':
        for i in range(t):
            pos_n[tick] = pos_n[tick - 1] + 1 
            tick += 1

for i in range(tick, 1000001):
    pos_n[tick] = pos_n[tick - 1]

pos_m = [0] * 1000001
tick = 1
for _ in range(m):
    t, d = input().split()
    t = int(t)

    if d == 'L':
        for i in range(t):
            pos_m[tick] = pos_m[tick - 1] - 1
            tick += 1
    elif d == 'R':
        for i in range(t):
            pos_m[tick] = pos_m[tick - 1] + 1
            tick += 1

for i in range(tick, 1000001):
    pos_m[tick] = pos_m[tick - 1]

cnt = 0
max_tick = max(len(pos_n), len(pos_m))

for i in range(1, max_tick):
    if i > 1 and pos_n[i] == pos_m[i] and pos_m[i - 1] != pos_n[i - 1]:
        cnt += 1

print(cnt)