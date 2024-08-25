import sys

n = int(input())
array = list(map(int, input().split()))

pluss = []
minuss = []
is_zero = False
for i in range(n):
    temp = array[i]

    if temp == 0:
        is_zero = True
    elif temp > 0:
        pluss.append(temp)
    else:
        minuss.append(temp)

pluss.sort(reverse=True)
minuss.sort()

ans = -sys.maxsize

if len(minuss) >= 3:
    ans = max(ans, minuss[-1] * minuss[-2] * minuss[-3])

if is_zero:
    ans = max(ans, 0)

if len(pluss) >= 3:
    ans = max(ans, pluss[0] * pluss[1] * pluss[2])

if len(minuss) >= 2 and len(pluss) >= 1:
    ans = max(ans, minuss[0] * minuss[1] * pluss[0])

print(ans)