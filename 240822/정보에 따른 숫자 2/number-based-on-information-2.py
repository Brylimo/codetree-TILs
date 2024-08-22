import sys

MAX_R = 1001
t, a, b = map(int, input().split())

line = [0] * MAX_R
s_pos = []
n_pos = []
ans = 0
for _ in range(t):
    c, x = input().split()
    x = int(x)

    if c == 'S':
        s_pos.append(x)
    elif c == 'N':
        n_pos.append(x)

for i in range(a, b + 1):
    dist_s = sys.maxsize
    for sx in s_pos:
        if abs(sx - i) < dist_s:
            dist_s = abs(sx - i)
    
    dist_n = sys.maxsize
    for nx in n_pos:
        if abs(nx - i) < dist_n:
            dist_n = abs(nx - i)

    if dist_s <= dist_n:
        ans += 1

print(ans)