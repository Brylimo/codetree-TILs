n, k = map(int, input().split())

array = [0] * 101
for _ in range(n):
    candy, pos = map(int, input().split())
    array[pos] += candy

ans = 0
for i in range(1, 101):
    left = (1 if i - k < 0 else i - k)
    right = (101 if i + k >= 100 else i + k + 1)

    sum_interval = 0
    for j in range(left, right):
        sum_interval += array[j]
    ans = max(ans, sum_interval)

print(ans)