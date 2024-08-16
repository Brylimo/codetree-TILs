import sys
input = sys.stdin.readline

string = input().rstrip()
line = list(string)

op_list = string.replace('+', '-').replace('*', '-').split('-')

array = []

def evaluate():
    idx = 0
    prev = 0
    opp = None
    for op in line:
        if ord('a') <= ord(op) <= ord('z'):
            if opp is None:
                prev += array[idx]
            elif opp == '-':
                prev -= array[idx]
            elif opp == '*':
                prev *= array[idx]
            else:
                prev += array[idx]
            idx += 1
        else:
            opp = op

    return prev

max_val = -int(1e9)
def calc(curr_num):
    global max_val
    if curr_num == len(op_list):
        res = evaluate()
        max_val = max(max_val, res)
        return

    for i in range(1, 5):
        array.append(i)
        calc(curr_num + 1)
        array.pop()

    return

calc(0)

print(max_val)