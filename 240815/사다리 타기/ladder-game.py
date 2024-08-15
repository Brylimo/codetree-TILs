import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

array = []
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    array.append((b, a))

array.sort()

def check_dest(segments):
    dest = []
    for i in range(1, n + 1):
        target = i
        for b, a in segments:
            if a == target:
                target += 1
            elif a == target - 1:
                target -= 1

        dest.append(target)

    return dest

real_dest = check_dest(array)

def is_dest_equal(real, temp):
    for i in range(len(real)):
        if real[i] != temp[i]:
            return False

    return True

answer = []
min_val = int(1e9)
def cal(curr_num):
    global min_val

    if curr_num == len(array):
        temp_dest = check_dest(answer)
        if is_dest_equal(real_dest, temp_dest):
            min_val = min(min_val, len(answer))
        return

    answer.append(array[curr_num])
    cal(curr_num + 1)
    answer.pop()

    cal(curr_num + 1)

cal(0)
print(min_val)