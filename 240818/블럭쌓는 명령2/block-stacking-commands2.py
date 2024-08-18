n, k = map(int, input().split())

array = [0] * (n + 1)
for _ in range(k):
    a, b = map(int, input().split())

    for i in range(a, b+1):
        array[i] += 1

print(max(array))