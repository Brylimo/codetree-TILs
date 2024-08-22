n, k = map(int, input().split())
bombs = []

for _ in range(n):
    bombs.append(int(input()))

ans = -1
kinds = list(set(bombs))
for num in kinds:
    loc = -1
    for i in range(n):
        if bombs[i] == num:
            if loc == -1:
                loc = i 
            else:
                if i - loc <= k:
                    ans = max(ans, num)
                    break

print(ans)