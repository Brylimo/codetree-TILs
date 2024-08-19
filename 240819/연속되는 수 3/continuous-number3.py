n = int(input())

array = []
for _ in range(n):
    x = int(input())
    array.append(x)

answer = 0
cnt = 1
for i in range(1, len(array)):
    if array[i - 1] > 0 and array[i] > 0:
        cnt += 1
    elif array[i - 1] < 0 and array[i] < 0:
        cnt += 1
    else:
        cnt = 1

    answer = max(answer, cnt)

print(answer)