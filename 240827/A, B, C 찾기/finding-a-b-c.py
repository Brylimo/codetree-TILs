array = list(map(int, input().split()))

array.sort()

a = array[0]
b = array[1]
c = array[-1] - (a + b)

print(a, b, c)