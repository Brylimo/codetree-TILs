n, m = map(int, input().split())
array = list(map(int, input().split()))

ans = 0

# 시작 위치
for i in range(1, n + 1):
    target = i - 1
    sum_value = 0
    for j in range(m):
        target = array[target]
        sum_value += target
        target -= 1

    ans = max(ans, sum_value)

print(ans)