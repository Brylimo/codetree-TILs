n, l = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

ans = 0
for i in range(n):
    cnt = 0
    temp = l
    for j in range(n):
        if array[j] >= array[i]:
            cnt += 1
        elif temp > 0 and array[j] + 1 >= array[i]:
            cnt += 1
            temp -= 1

    if cnt >= array[i]:
        ans = max(ans, array[i])

print(ans)