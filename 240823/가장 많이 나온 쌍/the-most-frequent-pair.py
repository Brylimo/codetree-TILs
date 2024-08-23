n, m = map(int, input().split())

points = []
for _ in range(m):
    a, b = map(int, input().split())
    if a < b:
        points.append((a, b))
    else:
        points.append((b, a))

ans = 0
for i in range(len(points)):
    cnt = 0
    for j in range(i + 1, len(points)):
        if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
            cnt += 1

    ans = max(ans, cnt + 1)

print(ans)