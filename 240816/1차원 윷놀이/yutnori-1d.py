import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))

arr = []
loc = [1] * (k + 1)
def score():
    for idx, target in enumerate(arr):
        loc[target] += array[idx]

    cnt = 0
    for i in range(1, k + 1):
        if loc[i] >= m:
            cnt += 1

    return cnt            

max_val = 0
def calc(curr_num):
    global max_val
    if curr_num == n:
        max_val = max(max_val, score())
        return

    for i in range(1, k):
        arr.append(i)
        calc(curr_num + 1)
        arr.pop()

calc(0)
print(max_val)