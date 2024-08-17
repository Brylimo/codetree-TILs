import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))

max_val = 0
combinations = []

def xor():
    result = combinations[0]
    for i in range(1, len(combinations)):
        result = result ^ combinations[i]

    return result

def calc(curr_num, cnt):
    global max_val
    if curr_num == n:
        if cnt == m:
            max_val = max(max_val, xor())
        return

    combinations.append(curr_num)
    calc(curr_num + 1, cnt + 1)
    combinations.pop()

    calc(curr_num + 1, cnt)

calc(0, 0)
print(max_val)