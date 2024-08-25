import sys

n = int(input())
seats = list(map(int, list(input())))

max_point = None
max_cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if seats[i] == 1 and seats[j] == 1:
            if max_cnt < j - i:
                max_cnt = j - i
                max_point = (i, j)
            break

ans = 0
# case 1. 가장 긴 거리의 가운데
seats[(max_point[0] + max_point[1]) // 2] = 1

temp = sys.maxsize
for i in range(n):
    for j in range(i + 1, n):
        if seats[i] == 1 and seats[j] == 1:
            temp = min(temp, j - i)
            break

ans = max(ans, temp)

seats[(max_point[0] + max_point[1]) // 2] = 0
# case 2. 왼쪽 끝에 1 추가
if seats[0] != 1:
    seats[0] = 1

    temp = sys.maxsize
    for i in range(n):
        for j in range(i + 1, n):
            if seats[i] == 1 and seats[j] == 1:
                temp = min(temp, j - i)
                break
    ans = max(ans, temp)

    seats[0] = 0
# case 3. 오른쪽 끝에 1 추가
if seats[-1] != 1:
    seats[-1] = 1

    temp = sys.maxsize
    for i in range(n):
        for j in range(i + 1, n):
            if seats[i] == 1 and seats[j] == 1:
                temp = min(temp, j - i)
                break
    ans = max(ans, temp)

    seats[-1] = 0

print(ans)