n = int(input())

a, b = 0, 0
cnt = 0
status = 0 # draw
for _ in range(n):
    c, s = input().split()
    s = int(s)

    if c == 'A':
        a += s
    elif c == 'B':
        b += s 

    if a == b and status != 0:
        cnt += 1
        status = 0
    elif a > b and status != 1:
        cnt += 1
        status = 1
    elif a < b and status != 2:
        cnt += 1
        status = 2

print(cnt)