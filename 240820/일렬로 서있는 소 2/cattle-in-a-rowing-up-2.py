n = int(input())
array = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if array[i] <= array[j] <= array[k]:
                cnt += 1

print(cnt)