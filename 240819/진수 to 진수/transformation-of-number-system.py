a, b = map(int, input().split())
digits = list(map(int, list(input())))

num = 0
for i in digits:
    num = num * a + i 

array = []
while True:
    if num < b:
        array.append(num)
        break

    array.append(num % b)
    num = num // b

for k in array[::-1]:
    print(k, end="")