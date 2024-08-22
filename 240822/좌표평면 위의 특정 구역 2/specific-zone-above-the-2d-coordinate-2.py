import sys
n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

ans = sys.maxsize
for i in range(n):
    min_x = sys.maxsize
    min_y = sys.maxsize
    max_x = 0
    max_y = 0

    for j in range(n):
        if i == j:
            continue

        ax, ay = points[j]

        min_x = min(min_x, points[j][0])
        max_x = max(max_x, points[j][0])
        
        min_y = min(min_y, points[j][1])
        max_y = max(max_y, points[j][1])

    ans = min(ans, (max_x - min_x) * (max_y - min_y))

print(ans)