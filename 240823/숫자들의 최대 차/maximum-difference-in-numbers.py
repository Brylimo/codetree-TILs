n, k = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))

ans = 0
for i in range(1, 10001):
    a = i 
    b = i + k

    cnt = 0
    for j in range(n):
        if a <= array[j] <= b:
            cnt += 1

    ans = max(ans, cnt)

print(ans)