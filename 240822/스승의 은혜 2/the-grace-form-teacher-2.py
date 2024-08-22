n, b = map(int, input().split())

p_array = []
for _ in range(n):
    p_array.append(int(input()))

ans = 0
p_array.sort()
for i in range(n):
    temp = 0
    cnt = 0
    for j in range(n):
        if i == j:
            temp += p_array[i] // 2

        temp += p_array[j]
        cnt += 1

        if temp > b:
            break

    ans = max(ans, cnt)

print(ans)