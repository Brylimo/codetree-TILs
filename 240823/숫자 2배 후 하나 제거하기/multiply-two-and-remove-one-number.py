n = int(input())
array = list(map(int, input().split()))

ans = int(1e9)
# 2배할 숫자를 고름
for i in range(n):
    array[i] *= 2
    for k in range(n):
        remaining_arr = []
        for t in range(n):
            if k == t:
                continue

            remaining_arr.append(array[t])

        sum_val = 0
        for t in range(n - 2):
            sum_val += abs(remaining_arr[t] - remaining_arr[t + 1])

        ans = min(ans, sum_val)

    array[i] //= 2

print(ans)