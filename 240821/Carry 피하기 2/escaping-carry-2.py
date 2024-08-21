n = int(input())

num_list = []
array = []
for i in range(n):
    numbers = input()
    array.append(list(reversed(list(map(int, list(numbers))))))
    num_list.append(int(numbers))

def check(a, b):
    length = min(len(a), len(b))

    for i in range(length):
        if a[i] + b[i] > 9:
            return False

    return True

ans = -1
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if check(array[k], array[j]):
                temp = num_list[k] + num_list[j]

                if check(list(reversed(list(map(int, list(str(temp)))))), array[i]):
                    ans = max(ans, temp + num_list[i])

print(ans)