import sys
input = sys.stdin.readline

string = input().rstrip()
line = list(string)

op_list = string.replace('+', '-').replace('*', '-').split('-')

array = []

def evaluate(length):
    prev = 0
    opp = '+'
    
    for op in line:
        if ord('a') <= ord(op) <= ord('f'):
            if opp == '-':
                prev -= array[ord(op) - ord('a')]
            elif opp == '*':
                prev *= array[ord(op) - ord('a')]
            else:
                prev += array[ord(op) - ord('a')]
        else:
            opp = op

    return prev

max_val = -int(1e9)
def calc(curr_num):
    global max_val
    if curr_num == len(set(op_list)):
        res = evaluate(len(set(op_list)))
        max_val = max(max_val, res)
        return

    for i in range(1, 5):
        array.append(i)
        calc(curr_num + 1)
        array.pop()

    return

calc(0)

print(max_val)