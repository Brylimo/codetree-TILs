import sys

x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

min_x = sys.maxsize
max_x = 0
min_y = sys.maxsize
max_y = 0

min_x = min(x1, x2, a1, a2)
max_x = max(x1, x2, a1, a2)
min_y = min(y1, y2, b1, b2)
max_y = max(y1, y2, b1, b2)

print((max_x - min_x) * (max_y - min_y))