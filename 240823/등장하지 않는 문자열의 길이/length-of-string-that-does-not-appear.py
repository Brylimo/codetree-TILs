n = int(input())
array = list(input())

ans = 0
# 연속 부분문자열 개수
for i in range(1, 101):
    correct = True
    for j in range(n - i + 1):
        string = array[j:j+i]
        for k in range(j + 1, n - i + 1):
            if string == array[k:k+i]:
                correct = False
                break

        if not correct:
            break

    if correct:
        ans = i
        break 

print(ans)