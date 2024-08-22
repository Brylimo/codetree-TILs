n = int(input())

h = []
for _ in range(n):
    h.append(int(input()))

ans = 0
for i in range(1, 1001):
    flag = False
    cnt = 0
    for j in range(len(h)):
        if flag == False and i < h[j]:
            flag = True
            cnt += 1
        
        if flag and i >= h[j]:
            flag = False

    ans = max(ans, cnt)

print(ans)