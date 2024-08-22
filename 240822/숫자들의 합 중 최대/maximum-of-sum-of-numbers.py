x, y = map(int, input().split())

ans = 0
for num in range(x, y+1):
    sum_value = sum(list(map(int, list(str(num)))))
    ans = max(ans, sum_value)

print(ans)