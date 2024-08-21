import sys
array = list(map(int, input().split()))

ans = sys.maxsize
sum_value = sum(array)
for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            one = array[i] + array[j] + array[k]
            other = sum_value - one

            ans = min(ans, abs(one - other))

print(ans)