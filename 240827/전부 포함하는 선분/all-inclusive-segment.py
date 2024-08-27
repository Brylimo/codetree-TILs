import sys

n = int(input())

points = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    points.append((x1, x2))

ans = sys.maxsize
for i in range(n):
    min_point = sys.maxsize
    max_point = 0
    for j in range(n):
        if i == j:
            continue

        min_point = min(min_point, points[j][0])
        max_point = max(max_point, points[j][1])

    ans = min(ans, max_point - min_point)

print(ans)