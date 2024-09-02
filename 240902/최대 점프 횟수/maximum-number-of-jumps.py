n = int(input())
array = list(map(int, input().split()))

dp = [0] * n
for i in range(1, n):
    for j in range(i):
        if j != 0 and dp[j] == 0:
            continue

        if j + array[j] >= i:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))