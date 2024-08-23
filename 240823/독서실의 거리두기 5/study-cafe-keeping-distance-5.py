n = int(input())
seats = list(map(int, list(input())))

ans = 0
for i in range(n):
    if seats[i] == 0:
        seats[i] = 1
    else:
        continue

    sub = int(1e9)
    cnt = 0
    for j in range(n):
        if seats[j] == 1 and cnt == 0:
            cnt = 1
        elif seats[j] == 0 and cnt > 0:
            cnt += 1
        elif seats[j] == 1 and cnt > 0:
            sub = min(sub, cnt)
            cnt = 1
    
    seats[i] = 0
    ans = max(ans, sub)

print(ans)