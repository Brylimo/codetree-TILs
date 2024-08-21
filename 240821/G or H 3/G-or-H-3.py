n, k = map(int, input().split())

array = [0] * 10001
for _ in range(n):
    l, a = input().split()
    l = int(l)

    if a == 'G':
        array[l] = 1
    elif a == 'H':
        array[l] = 2

ans = 0
for i in range(1, 10001 - k):
    sum_value = 0
    for j in range(k + 1):
        sum_value += array[i + j]
    ans = max(ans, sum_value)

print(ans)