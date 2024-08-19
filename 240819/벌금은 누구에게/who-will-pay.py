n, m, k = map(int, input().split())

array = [0] * (n + 1)
ans = -1
for _ in range(m):
    x = int(input())

    array[x] += 1

    if array[x] >= k:
        ans = x
        break

print(ans)