n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0
b.sort()
for i in range(n - m + 1):
    sum_interval = []
    for k in range(i, i + m):
        sum_interval.append(a[k])
    
    sum_interval.sort()
    flag = True
    for i in range(m):
        if b[i] != sum_interval[i]:
            flag = False
            break

    if flag:
        cnt += 1

print(cnt)