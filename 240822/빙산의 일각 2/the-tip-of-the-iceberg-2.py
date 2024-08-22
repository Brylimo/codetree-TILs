n = int(input())

h = []
for _ in range(n):
    h.append(int(input()))

ans = 0
for i in range(1, 1001):
    cnt = 1
    for j in range(len(h) - 1):
        if i < h[j] and i >= h[j + 1]:
            cnt += 1

    ans = max(ans, cnt)

print(ans)