import sys
n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

ans = sys.maxsize
for i in range(n):
    for j in range(n):
        if i == j:
            continue

        ans = min(ans, (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)

print(ans)