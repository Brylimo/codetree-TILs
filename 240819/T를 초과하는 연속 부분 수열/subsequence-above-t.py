n, t = map(int, input().split())
array = list(map(int, input().split()))

cnt, ans = 0, 0
for i in range(n):
    if i > 0 and array[i] > t:
        cnt += 1
    elif i == 0 and array[0] > t:
        cnt = 1
    else:
        cnt = 0

    ans = max(ans, cnt)

print(ans)