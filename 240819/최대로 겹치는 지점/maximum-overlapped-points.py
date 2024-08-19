n = int(input())

line = [0] * (101)
for _ in range(n):
    x1, x2 = map(int, input().split())
    for k in range(x1, x2 + 1):
        line[k] += 1

answer = 0
for i in range(101):
    answer = max(answer, line[i])

print(answer)