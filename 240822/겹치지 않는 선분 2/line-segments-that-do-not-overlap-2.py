n = int(input())

points = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    points.append((x1, x2))

cnt = 0
for i, (ix1, ix2) in enumerate(points):
    for j, (jx1, jx2) in enumerate(points, start = i + 1):
        if (ix1 < jx1 and ix2 > jx2) or (ix1 < jx1 < ix2):
            cnt += 1

print(cnt)