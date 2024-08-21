n, h, t = map(int, input().split())

array = list(map(int, input().split()))

ans = int(1e9)
for i in range(n):
    energy = 0
    flag = True
    for j in range(i, i + t):
        if j >= n:
            flag = False
            break

        energy += abs(array[j] - h)
    if flag:
        ans = min(ans, energy)

print(ans)