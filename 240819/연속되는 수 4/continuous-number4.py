n = int(input())

array = []
for _ in range(n):
    x = int(input())
    array.append(x)

cnt, ans = 0, 0
for i in range(n):
    if i > 0 and array[i] > array[i - 1]:
        cnt += 1
    else:
        cnt = 1

    ans = max(ans, cnt)

print(ans)