a, b, c = map(int, input().split())

ans = 0
for i in range(1000):
    for j in range(1000):
        temp = a * i + b * j

        if temp > c:
            continue

        ans = max(ans, temp)

print(ans)