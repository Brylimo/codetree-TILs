import sys
n = int(input().rstrip())
array = list(map(int, input().rstrip().split()))

seq = []
min_value = sys.maxsize
def calc(curr_num):
    global min_value

    if curr_num >= n:
        return
    jump_cnt = array[curr_num]

    if sum(seq) + 1 > n:
            return
    elif sum(seq) + 1 == n:
        min_value = min(min_value, len(seq))
        return
    
    for i in range(1, jump_cnt + 1):
        seq.append(i)
        calc(curr_num + i)
        seq.pop()

calc(0)
if min_value == sys.maxsize:
    print(-1)
else:
    print(min_value)