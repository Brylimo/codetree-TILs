a, b = map(int, input().split())
c, d = map(int, input().split())

line = [0] * 101

for i in range(a, b):
    line[i] = 1

for j in range(c, d):
    line[j] = 1

print(sum(line))