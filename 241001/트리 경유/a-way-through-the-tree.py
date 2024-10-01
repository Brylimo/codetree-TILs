n, q = map(int, input().split())
root = 1

tree = [0] * (n + 1)

ans = 0
def traverse(m):
    global ans

    if m == 1:
        return

    if tree[m] != 1:
        traverse(m // 2)
    else:
        ans = m
        traverse(m // 2)

for _ in range(q):
    mm = int(input())

    ans = 0
    traverse(mm)

    if not ans:
        tree[mm] = 1
        print(0)
    else:
        print(ans)