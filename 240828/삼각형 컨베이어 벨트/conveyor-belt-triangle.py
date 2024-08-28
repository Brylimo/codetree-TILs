n, t = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))

for _ in range(t):
    first_temp = first[-1]
    second_temp = second[-1]
    third_temp = third[-1]

    for i in range(n - 1, 0, -1):
        first[i] = first[i - 1]

    for i in range(n - 1, 0, -1):
        second[i] = second[i - 1]

    for i in range(n - 1, 0, -1):
        third[i] = third[i - 1]

    second[0] = first_temp
    third[0] = second_temp
    first[0] = third_temp

for i in range(n):
    print(first[i], end=" ")
print()
for i in range(n):
    print(second[i], end=" ")
print()
for i in range(n):
    print(third[i], end=" ")