n = int(input())

times = []
for _ in range(n):
    a, b = map(int, input().split())
    times.append((a, b))

ans = 0
for i in range(n):
    array = [0] * 1001
    for j in range(n):
        if i == j:
            continue

        for k in range(times[j][0], times[j][1]):
            array[k] = 1
        
    ans = max(ans, sum(array))

print(ans)