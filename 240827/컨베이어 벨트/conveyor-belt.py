n, t = map(int, input().split())
upper = list(map(int, input().split()))
lower = list(map(int, input().split()))

for i in range(t):
    u_temp = upper[-1]
    l_temp = lower[-1]

    for j in range(n - 1, 0, -1):
        upper[j] = upper[j - 1]

    for j in range(n - 1, 0, -1):
        lower[j] = lower[j - 1]

    upper[0] = l_temp
    lower[0] = u_temp

for i in range(n):
    print(upper[i], end=" ")
print()
for i in range(n):
    print(lower[i], end=" ")