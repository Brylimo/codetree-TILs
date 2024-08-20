array = list(map(int, list(input())))

def get_num(t_array):
    num = 0
    for i in range(len(t_array)):
        num = num * 2 + t_array[i]

    return num

ans = 0
for i in range(len(array)):
    array[i] = array[i] ^ 1

    ans = max(ans, get_num(array))
    array[i] = array[i] ^ 1

print(ans)