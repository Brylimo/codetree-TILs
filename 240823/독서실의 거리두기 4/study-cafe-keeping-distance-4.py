import sys

n = int(input())
seats = list(map(int, list(input())))

ans = 0
# 새로 두명을 더 받음
for i in range(n):
    for j in range(i + 1, n):
        if seats[i] != 0 or seats[j] != 0:
            if seats[i] == 1:
                break
            continue

        seats[i] = 1
        seats[j] = 1

        prev = -1
        dist = sys.maxsize
        for k in range(n):
            if seats[k] == 1:
                if prev == -1:
                    prev = k
                else:
                    dist = min(dist, abs(k - prev))
                    prev = k

        ans = max(ans, dist)
        seats[i] = 0
        seats[j] = 0

print(ans)