import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))

max_val = 0
combinations = []

def xor():
    result = 0
    for num in combinations:
        result = result ^ num

    return result

def calc(curr_num, cnt):
    global max_val
    if curr_num == n + 1:
        if cnt == m:
            max_val = max(max_val, xor())
        return

    combinations.append(curr_num)
    calc(curr_num + 1, cnt + 1)
    combinations.pop()

    calc(curr_num + 1, cnt)

calc(1, 0)
print(max_val)