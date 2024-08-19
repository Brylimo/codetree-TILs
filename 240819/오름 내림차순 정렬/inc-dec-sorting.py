n = int(input())
array = list(map(int, input().split()))

array.sort()
for k in array:
    print(k, end=" ")
print()

array.reverse()
for k in array:
    print(k, end=" ")