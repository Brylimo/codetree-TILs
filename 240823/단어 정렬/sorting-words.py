n = int(input())
array=[]
for _ in range(n):
    array.append(input())

array.sort()
for k in array:
    print(k)