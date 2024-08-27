import sys

n = int(input())
array = list(map(int, input().split()))
right = list(range(1, n + 1))

end = max(array)
if len(array) == 2:
    if array != right:
        print(1)
    else:
        print(0)

cnt = 0
while True:
    if right == array:
        break

    idx = 0
    min_val = sys.maxsize
    target = array.pop(0)
    for i in range(2, n - 1):
        if end == target:
            idx = n - 1
            break
        
        if array[i] > target and min_val > array[i] - target:
            min_val = array[i] - target
            idx = i

    array.insert(idx, target)
    cnt += 1

print(cnt)