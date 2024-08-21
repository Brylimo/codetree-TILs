n = int(input())
keys = list(map(int, input().split()))

cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if abs(keys[0] - i) <= 2 or abs(keys[1] - j) <= 2 or abs(keys[2] - k) <= 2:
                cnt += 1

print(cnt)