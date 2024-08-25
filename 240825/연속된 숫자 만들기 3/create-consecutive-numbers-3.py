a, b, c = map(int, input().split())

temp =[a, b, c]

ans = 0
while not (temp[0] + 1 == temp[1] and temp[1] + 1 == temp[2]):
    if abs(temp[1] - temp[0]) > abs(temp[2] - temp[1]):
        temp[1], temp[2] = temp[1] - 1, temp[1]
    else:
        temp[0], temp[1] = temp[1], temp[2] - 1

    ans += 1
print(ans)