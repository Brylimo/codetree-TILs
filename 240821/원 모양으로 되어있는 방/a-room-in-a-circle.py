n = int(input())

array = []

for _ in range(n):
    x = int(input())
    array.append(x)

ans = int(1e9)
for i in range(1, n + 1):
    dist = 0
    sum_val = 0

    cnt = i
    while not (cnt > i and (cnt - 1) % n == i - 1):
        sum_val += dist * array[(cnt - 1) % n]
        cnt += 1
        dist += 1

    ans = min(ans, sum_val)

print(ans)