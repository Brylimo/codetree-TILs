n, k = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0] * n

prefix_sum[0] = arr[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

max_val = 0
for i in range(k, n):
    max_val = max(max_val, prefix_sum[i] - prefix_sum[i - k + 1] + arr[i - k + 1])

print(max_val)