import sys
input = sys.stdin.readline

n = int(input().rstrip())
grid = [
    list(input().rstrip())
    for _ in range(n)
]

d = dict()
nums = []
for i in range(n):
    for j in range(n):
        if grid[i][j].isdigit():
            nums.append(int(grid[i][j]))
            d[int(grid[i][j])] = (i, j)
        elif grid[i][j] == 'S':
            start_point = (i, j)
        elif grid[i][j] == 'E':
            end_point = (i, j)

def calc_dist(a, b):
    x1, y1 = a
    x2, y2 = b

    return abs(x1 - x2) + abs(y1 - y2)

combinations = []
answer = sys.maxsize
def find_path(idx, cnt):
    global answer
    if cnt == 3:
        temp_dist = 0
        temp_dist += calc_dist(start_point, d[combinations[0]])
        for i in range(len(combinations) - 1):
            temp_dist += calc_dist(d[combinations[i]], d[combinations[i + 1]])
        temp_dist += calc_dist(d[combinations[-1]], end_point)
        answer = min(answer, temp_dist)
        return

    if idx == len(nums):
        return

    combinations.append(nums[idx])
    find_path(idx + 1, cnt + 1)
    combinations.pop()

    find_path(idx + 1, cnt)

find_path(0, 0)
if answer == sys.maxsize:
    print(-1)
else:
    print(answer)