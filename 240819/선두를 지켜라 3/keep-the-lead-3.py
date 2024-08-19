n, m = map(int, input().split())
MAX_R = 1000001

tick = 1
pos_n = [0] * MAX_R
for _ in range(n):
    v, t = map(int, input().split())
    for i in range(t):
        pos_n[tick] = pos_n[tick - 1] + v
        tick += 1
    
tick = 1
pos_m = [0] * MAX_R
for _ in range(m):
    v, t = map(int, input().split())
    for i in range(t):
        pos_m[tick] = pos_m[tick - 1] + v
        tick += 1

leader, cnt = (1 if pos_m[1] > pos_n[1] else 2), 1
for i in range(2, tick):
    if pos_m[i] < pos_n[i] and leader != 2:
        cnt += 1
        leader = 2
    elif pos_m[i] > pos_n[i] and leader != 1:
        cnt += 1
        leader = 1
    elif pos_m[i] == pos_n[i] and pos_m[i - 1] != pos_n[i - 1]:
        cnt += 1
        leader = 3

print(cnt)