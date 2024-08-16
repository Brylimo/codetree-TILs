import sys
n = int(input().rstrip())
array = list(map(int, input().rstrip().split()))

seq = []
min_value = sys.maxsize
def calc(curr_num):
    global min_value
    jump_cnt = array[curr_num]

    for i in range(1, jump_cnt + 1):
        if sum(seq) + 1 > n:
            return
        if sum(seq) + 1 == n:
            min_value = min(min_value, len(seq))
            return
        else:
            seq.append(i)
            calc(curr_num + 1)
            seq.pop()

calc(0)
if min_value == sys.maxsize:
    print(-1)
else:
    print(min_value)