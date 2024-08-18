import sys
n = int(input().rstrip())

offset = 100
checked = [0] * 201
for _ in range(n):
    x1, x2 = map(int, input().rstrip().split())
    for i in range(x1, x2):
        checked[i + 100] += 1

print(max(checked))