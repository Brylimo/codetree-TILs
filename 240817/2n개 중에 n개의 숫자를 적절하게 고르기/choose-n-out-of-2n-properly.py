import sys
input = sys.stdin.readline

n = int(input().rstrip())
array = list(map(int, input().rstrip().split()))

seq = []
total = sum(array)
min_val = sys.maxsize
def calc(curr_idx, cnt):
    global min_val
    if curr_idx >= 2 * n:
        return

    if cnt == n:
        sub1 = sum(seq)
        sub2 = total - sub1

        min_val = min(min_val, abs(sub1 - sub2))
        return

    seq.append(array[curr_idx])
    calc(curr_idx + 1, cnt + 1)
    seq.pop()

    calc(curr_idx + 1, cnt)

calc(0, 0)
print(min_val)