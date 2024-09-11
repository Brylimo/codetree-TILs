import sys
INT_MIN = -sys.maxsize

n = int(input())
nums = list(map(int, input().split()))

total = sum(nums)
dp = [INT_MIN] * (total + 1)
dp[0] = 0

for j in range(n):
    for i in range(total, -1, -1):
        if i >= nums[j]:
            if dp[i - nums[j]] == INT_MIN:
                continue
            
            dp[i] = 1

for i in range(total):
    other = total - i
    if other == i:
        print("Yes")
        sys.exit(0)
        
print("No")