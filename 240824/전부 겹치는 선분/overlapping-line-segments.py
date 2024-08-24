n = int(input())

lines = [0] * 101
for _ in range(n):
    x1, x2 = map(int, input().split())
    for i in range(x1, x2 + 1):
        lines[i] += 1

if max(lines) == n:
    print("Yes")
else:
    print("No")