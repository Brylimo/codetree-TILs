import sys

n = int(input())

points = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    points.append((x1, x2))

for i in range(n):
    max_x1 = 0
    min_x2 = sys.maxsize
    for j in range(n):
        if i == j:
            continue

        max_x1 = max(max_x1, points[j][0])
        min_x2 = min(min_x2, points[j][1])

    if max_x1 <= min_x2:
        print("Yes")
        sys.exit(0)

print("No")