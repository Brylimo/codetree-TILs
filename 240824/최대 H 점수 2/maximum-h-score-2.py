n, l = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

ans = 0
for i in range(101):
    cnt = 0
    temp = l
    for j in range(n):
        if array[j] >= i:
            cnt += 1
        elif temp > 0 and array[j] + 1 >= i:
            cnt += 1
            temp -= 1

    if cnt >= i:
        ans = max(ans, i)

print(ans)