n, q = map(int, input().split())
root = 1

tree = [0] * (n + 1)

def traverse(m):
    if m == 1:
        return 0

    if tree[m] != 1:
        return traverse(m // 2)
    else:
        return m


for _ in range(q):
    m = int(input())

    rst = traverse(m)

    if not rst:
        tree[m] = 1
        print(0)
    else:
        print(rst)