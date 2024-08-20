import sys

n = int(input())
array = list(map(int, input().split()))

ans = sys.maxsize
for i in range(n):
    sum_val = 0
    for j in range(n):
        dist = abs(i - j)
        sum_val += dist * array[j]
    ans = min(ans, sum_val)

print(ans)