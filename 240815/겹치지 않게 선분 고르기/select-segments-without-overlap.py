import sys
input = sys.stdin.readline

n = int(input().rstrip())
candidates = []
for _ in range(n):
    x, y = map(int, input().rstrip().split())
    candidates.append((x, y))

big_line = [0] * 1001

def is_overlap(curr_line):
    x1, x2 = candidates[curr_line]

    if any(i == 1 for i in big_line[x1:(x2 + 1)]):
        return True
    else:
        for i in range(x1, x2 + 1):
            big_line[i] = 1

        return False

max_cnt = 0

def cal(curr_line, count):
    global max_cnt
    if curr_line == n:
        return

    x1, x2 = candidates[curr_line]

    if not is_overlap(curr_line):
        max_cnt = max(max_cnt, count + 1)
        for i in range(curr_line + 1, len(candidates)):
            cal(i, count+1)
        for i in range(x1, x2 + 1):
            big_line[i] = 0

    return

for i in range(0, len(candidates)):
    cal(i, 0)
print(max_cnt)