x, y = map(int, input().split())

cnt = 0
for num in range(x, y + 1):
    digit = list(str(num))
    reverse = list(reversed(digit))
    
    correct = True
    for i in range(len(digit)):
        if digit[i] != reverse[i]:
            correct = False
            break

    if correct:
        cnt += 1
print(cnt)