n, k = map(int, input().split())

array = [0] * 101
for _ in range(n):
    candy, pos = map(int, input().split())
    array[pos] += candy

ans = 0
for i in range(k + 1, 101 - k - 1):
    sum_interval = 0
    for j in range(i - k, i + k + 1):
        sum_interval += array[j]
    ans = max(ans, sum_interval)

print(ans)