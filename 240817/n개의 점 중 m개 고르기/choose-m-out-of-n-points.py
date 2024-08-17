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
            temp = 0
            i_dix = 0
            j_idx = 0
            for i in range(m - 1):
                for j in range(i + 1, m):
                    if temp < abs(seq[i][0] - seq[j][0]) ** 2 + abs(seq[i][1] - seq[j][1]) ** 2:
                        i_idx = i 
                        j_idx = j
                        temp = abs(seq[i][0] - seq[j][0]) ** 2 + abs(seq[i][1] - seq[j][1]) ** 2

            min_val = min(min_val, get_min_dist(seq[i_idx], seq[j_idx]))
            return
        return

    seq.append(points[curr_idx])
    select_point(curr_idx + 1, cnt + 1)
    seq.pop()

    select_point(curr_idx + 1, cnt)

select_point(0, 0)
print(min_val)