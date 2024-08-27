array = list(map(int, input().split()))
array.sort()

a = array[0]
b = array[1]
c = array[2]
d = array[-1] - (a + b + c)

print(a, b, c, d)