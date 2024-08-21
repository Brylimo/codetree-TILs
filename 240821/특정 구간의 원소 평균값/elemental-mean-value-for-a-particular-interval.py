n = int(input())
array = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i, n):
        avg = sum(array[i:j+1]) / (j - i + 1)

        if avg in array[i:j+1]:
            cnt += 1

print(cnt)