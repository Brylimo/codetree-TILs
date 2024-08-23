n = int(input())

ranges = []
for _ in range(n):
    a, b = map(int, input().split())
    ranges.append((a, b))

ans = int(1e9)
for i in range(1, 10001):
    target = i * 2

    correct = True
    for j in range(n):
        if not (ranges[j][0] <= target <= ranges[j][1]):
            correct = False
            break
        else:
            target = target * 2
        
    if correct:
        ans = min(ans, i)

print(ans)