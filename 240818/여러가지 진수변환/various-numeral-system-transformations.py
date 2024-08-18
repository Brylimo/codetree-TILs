n, b = map(int, input().split())

digits = []
while True:
    if n < b:
        digits.append(n)
        break

    digits.append(n % b)
    n = n // b

for i in digits[::-1]:
    print(i, end="")