import sys
input = sys.stdin.readline

N, K, P, T = map(int, input().rstrip().split())
order = []
for _ in range(T):
    t, x, y = map(int, input().rstrip().split())
    order.append((t, x, y))

cnt = K
ans = [P]
order.sort()
for at, ax, ay in order:
    if ax == P and cnt > 0:
        cnt -= 1
        ans.append(ay)
    elif ay == P and cnt > 0:
        cnt -= 1
        ans.append(ax)

for i in range(1, N + 1):
    if i in ans:
        print(1, end="")
    else:
        print(0, end="")