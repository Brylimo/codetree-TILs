n = int(input())

sequence = []

def is_possible():
    for k in range(1, n // 2 + 1):
        for j in range(0, n - k, 1):
            if str(sequence[j:j+k]) == str(sequence[j+k:j+2*k]):
                return False

    return True

result = []
def calc(curr_num):
    if curr_num == n:
        if is_possible():
            result.append(tuple(sequence))
        return

    for i in range(4, 7):
        sequence.append(i)
        calc(curr_num + 1)
        sequence.pop()

    return

calc(0)
result.sort()
for i in range(len(result[0])):
    print(result[0][i], end="")