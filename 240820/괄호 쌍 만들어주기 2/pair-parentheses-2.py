array = list(input())

cnt = 0
for i in range(len(array)):
    for j in range(i + 2, len(array) - 1):
        if i + 1 < len(array) and j - 1 < len(array):
            if array[i] == '(' and array[i+1] == '(' and array[j] == ')' and array[j+1] == ')':
                cnt += 1

print(cnt)