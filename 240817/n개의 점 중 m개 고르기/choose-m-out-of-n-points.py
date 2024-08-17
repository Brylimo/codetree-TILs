import sys
import math
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

points = []
for _ in range(n):
    x, y = map(int, input().rstrip().split())
    points.append((x, y))

def get_min_dist(a, b):
    x1, y1 = a 
    x2, y2 = b

    return (x1 - x2) ** 2 + (y1 - y2) ** 2

seq = []
min_val = sys.maxsize
def select_point(curr_idx, cnt):
    global min_val
    if curr_idx == n:
        if cnt == m:
            seq.sort()
            min_val = min(min_val, get_min_dist(seq[0], seq[-1]))
            return
        return

    seq.append(points[curr_idx])
    select_point(curr_idx + 1, cnt + 1)
    seq.pop()

    select_point(curr_idx + 1, cnt)

select_point(0, 0)
print(min_val)