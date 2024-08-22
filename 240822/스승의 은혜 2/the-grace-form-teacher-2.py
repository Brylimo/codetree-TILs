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
            temp += p_array[j] // 2
            if temp > b:
                break

            cnt += 1
            continue

        temp += p_array[j]

        if temp > b:
            break

        cnt += 1

    ans = max(ans, cnt)

print(ans)