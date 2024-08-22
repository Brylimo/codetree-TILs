import sys

n = int(input())

points= []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            one = points[i]
            two = points[j]
            three = points[k]

            if (one[0] == two[0] or two[0] == three[0] or one[0] == three[0]) and (one[1] == two[1] or two[1] == three[1] or one[1] == three[1]):
                min_x = min(one[0], two[0], three[0])
                max_x = max(one[0], two[0], three[0])
                min_y = min(one[1], two[1], three[1])
                max_y = max(one[1], two[1], three[1])

                ans = max(ans, (max_x - min_x) * (max_y - min_y))

print(ans)