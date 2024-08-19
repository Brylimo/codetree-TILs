n, m = map(int, input().split())

pos_a = [0]
loc_a = 0
for _ in range(n):
    v, t = map(int, input().split())
    for i in range(t):
        loc_a += v
        pos_a.append(loc_a)

pos_b = [0]
loc_b = 0
for _ in range(m):
    v, t = map(int, input().split())
    for i in range(t):
        loc_b += v
        pos_b.append(loc_b)

cnt = 0
min_tick = min(len(pos_a), len(pos_b))
flag = 0
for i in range(1, min_tick):
    if i > 1 and pos_a[i] > pos_b[i] and flag == 1:
        cnt += 1
        flag = 0
    elif i > 1 and pos_a[i] < pos_b[i] and flag == 0:
        cnt += 1
        flag = 1
    elif i == 1 and pos_a[1] != pos_b[1]:
        if pos_a[1] < pos_b[1]:
            flag = 1
        else:
            flag = 0
    
print(cnt)