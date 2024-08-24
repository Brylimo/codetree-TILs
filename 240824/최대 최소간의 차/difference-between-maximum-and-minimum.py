import sys

n, k = map(int, input().split())
array = list(map(int, input().split()))

ans = sys.maxsize
for i in range(10001):
    a = i 
    b = i + k

    cost = 0
    for j in range(n):
        if a <= array[j] <= b:
            pass
        elif array[j] < a:
            cost += abs(a - array[j])
        elif b < array[j]:
            cost += abs(array[j] - b)

    ans = min(ans, cost)

print(ans)