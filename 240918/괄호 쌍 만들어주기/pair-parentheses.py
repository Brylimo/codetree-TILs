a = list(input())

R = [0] * len(a)

max_val = 0
cnt = 0
for i in range(len(a) - 1, -1, -1):
    if a[i] == ')':
        cnt += 1

        if cnt == 2:
            max_val += 1
            cnt = 1
    else:
        cnt = 0

    R[i] = max_val

ans = 0
cnt = 0
for i in range(len(a)):
    if a[i] == '(':
        cnt += 1

        if cnt == 2:
            ans += R[i]
            cnt = 1
    else:
        cnt = 0

print(ans)