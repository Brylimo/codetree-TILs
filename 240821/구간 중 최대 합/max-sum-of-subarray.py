n, k = map(int, input().split())
array = list(map(int, input().split()))

ans = 0
for i in range(n - k + 1):
    sum_value = 0
    for j in range(k):
        sum_value += array[i + j]
    
    ans = max(ans, sum_value)

print(ans)