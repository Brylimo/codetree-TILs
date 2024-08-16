import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))

arr = []
loc = [1] * (k + 1)
def score():
    global loc
    for idx, target in enumerate(arr):
        loc[target] += array[idx]

    cnt = 0
    for i in range(1, k + 1):
        if loc[i] >= m:
            cnt += 1

    loc = [1] * (k + 1)
    return cnt            

max_val = 0
def calc(curr_num):
    global max_val
    if curr_num == n:
        max_val = max(max_val, score())
        return

    for u in range(1, k + 1):
        arr.append(u)
        calc(curr_num + 1)
        arr.pop()

calc(0)
print(max_val)