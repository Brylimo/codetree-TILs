n = int(input())
array = list(input())

cnt = 0
for i in range(len(array)):
    for j in range(i + 1, len(array)):
        for k in range(j + 1, len(array)):
            if array[i] == 'C' and array[j] == 'O' and array[k] == 'W':
                cnt += 1

print(cnt)