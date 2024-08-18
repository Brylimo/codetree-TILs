digits = list(map(int, list(input())))

num = 0
for k in digits:
    num = num * 2 + k

num *= 17


digit_arr = []
while True:
    if num < 2:
        digit_arr.append(num)
        break

    digit_arr.append(num % 2)
    num //= 2

for d in digit_arr[::-1]:
    print(d, end="")