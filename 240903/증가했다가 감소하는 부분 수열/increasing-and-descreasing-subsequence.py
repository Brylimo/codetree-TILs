n = int(input())
nums = list(map(int, input().split()))

dp = [
    [0] * 2
    for _ in range(n)
]

# 첫번째 원소 초기화, 증가하는 개수 0, 감소하는 개수 0
dp[0][0], dp[0][1] = 1, 1

for i in range(n):
    for j in range(i):
        # 증가하는 경우
        if nums[j] < nums[i]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        elif nums[j] > nums[i]:
            dp[i][1] = max(dp[i][1], dp[j][0] + 1, dp[j][1] + 1)

print(max([
    dp[i][j]
    for i in range(n)
    for j in range(2)
]))