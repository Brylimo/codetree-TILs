array = list(input())

cnt = 0
n = len(array)
for i in range(n - 1):
    for j in range(i + 1, n):
        if array[i] == '(' and array[j] == ')':
            cnt += 1

print(cnt)