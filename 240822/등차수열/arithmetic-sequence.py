from collections import Counter
n = int(input())
array = list(map(int, input().split()))

ans = 0
for k in range(1, 101):
    dist = []
    for i in range(n):
        dist.append(abs(array[i] - k))

    cnt = 0
    c = Counter(dist)
    for v in c.values():
        if v > 1:
            cnt += 1

    ans = max(ans, cnt)

print(ans)