n, k = map(int, input().split())

bombs = []
for _ in range(n):
    bombs.append(int(input()))

candidates = list(set(bombs))
candidates.sort()

ans = 0
result = 0
for i in candidates:
    prev = -1
    cnt = 0
    for j in range(n):
        if bombs[j] == i:
            if prev == -1:
                prev = j
            else:
                dist = j - prev
                if dist <= k:
                    cnt += 1

    if cnt != 0 and cnt >= result:
        result = cnt
        ans = i 

print(ans)