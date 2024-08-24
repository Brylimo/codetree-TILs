import sys
n = int(input())

hills = []
for _ in range(n):
    hills.append(int(input()))

ans = sys.maxsize
for i in range(101):
    a = i 
    b = i + 17

    cost = 0
    for j in range(n):
        if a <= hills[j] <= b:
            pass
        elif hills[j] < a:
            cost += (a - hills[j]) ** 2
        elif b < hills[j]:
            cost += (hills[j] - b) ** 2

    ans = min(ans, cost)

print(ans)