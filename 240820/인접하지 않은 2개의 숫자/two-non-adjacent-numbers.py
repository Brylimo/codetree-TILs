n = int(input())
array = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if j == i + 1:
            continue
        else:
            ans = max(ans, array[i] + array[j])

print(ans)