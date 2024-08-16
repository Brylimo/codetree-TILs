import sys
input = sys.stdin.readline

k, n = map(int, input().rstrip().split())

arr = []
result = []
def print_num():
    result.append(tuple(arr))
    return

def calc(curr_num):
    if curr_num == n + 1:
        print_num()
        return

    for i in range(1, k + 1):
        if not (len(arr) >= 2 and (arr[-1] == arr[-2]) and (arr[-1] == i)):
            arr.append(i)
            calc(curr_num + 1)
            arr.pop()

calc(1)
result.sort()
for t in result:
    for i in range(len(t)):
        print(t[i], end=" ")
    print()