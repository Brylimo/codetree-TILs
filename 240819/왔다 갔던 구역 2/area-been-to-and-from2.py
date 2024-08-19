n = int(input())


line = [0] * 1001
cur = 0
for _ in range(n):
    x, dir = input().split()

    x = int(x)
    if dir == 'R':
        for i in range(cur, cur + x - 1):
            line[i] += 1
    elif dir == 'L':
        for i in range(cur + 1, cur - x + 1, -1):
            line[i - 1] += 1

cnt = 0
for i in range(len(line)):
    if line[i] >= 2:
        cnt += 1

print(cnt)