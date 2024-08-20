import sys
from copy import deepcopy
n = int(input())

array = []
for _ in range(n):
    x, y = map(int, input().split())
    array.append((x, y))

def get_distance(array):
    dist = 0
    for i in range(n - 2):
        x1, y1 = array[i]
        x2, y2 = array[i + 1]

        dist += abs(x1 - x2) + abs(y1 - y2)

    return dist

ans = sys.maxsize
for i in range(1, n - 1):
    varray = deepcopy(array)
    
    varray.pop(i)
    ans = min(ans, get_distance(varray))

print(ans)