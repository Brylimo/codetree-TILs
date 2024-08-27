x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

max_x = max(x1, x2, a1, a2)
max_y = max(y1, y2, b1, b2)
min_x = min(x1, x2, a1, a2)
min_y = min(y1, y2, b1, b2)

part = max((max_x - min_x), (max_y - min_y))
print(part ** 2)