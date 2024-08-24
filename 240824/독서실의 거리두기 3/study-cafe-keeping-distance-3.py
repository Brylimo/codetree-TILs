n = int(input())
seats = list(map(int, list(input())))

dist = 0
star = None
cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if seats[i] == 1 and seats[j] == 1:
            if dist < j - i:
                dist = j - i
                star = (i, j)
            break

seats[(star[0] + star[1]) // 2] = 1

ans = int(1e9)
for i in range(n - 1):
    for j in range(i + 1, n):
        if seats[i] == 1 and seats[j] == 1:
            ans = min(ans, j - i)
            break

print(ans)