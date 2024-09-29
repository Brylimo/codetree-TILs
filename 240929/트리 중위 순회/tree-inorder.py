k = int(input())

left = [0] * (2 ** k)
right = [0] * (2 ** k)
array = list(map(int, input().split()))

root = -1

tree = [[] for _ in range(k)]

def calculate(arr, value, dir):
    global root

    if len(arr) <= 0:
        return

    idx = len(arr) // 2

    if value == -1:
        root = arr[idx]
    else:
        if dir == 0:
            left[value] = arr[idx]
        else:
            right[value] = arr[idx]

    calculate(arr[:idx], arr[idx], 0)
    calculate(arr[idx + 1:], arr[idx], 1)

def preorder(x, step):
    if x == 0:
        return

    tree[step].append(x)
    preorder(left[x], step + 1)
    preorder(right[x], step + 1)

calculate(array, root, 0)
preorder(root, 0)

for i in range(len(tree)):
    for j in range(len(tree[i])):
        print(tree[i][j], end=" ")
    print()