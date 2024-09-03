n, m = map(int, input().split())
seq = list(map(int, input().split()))

dp = [0] * (m + 1)
dp[0] = 1

for i in range(n):
    for j in range(m, -1, -1):
        if j >= seq[i]:
            dp[j] += dp[j - seq[i]]

if dp[m] != 0:
    print("Yes")
else:
    print("No")