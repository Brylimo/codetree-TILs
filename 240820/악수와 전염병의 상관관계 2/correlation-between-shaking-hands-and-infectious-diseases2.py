import sys
input = sys.stdin.readline

N, K, P, T = map(int, input().rstrip().split())
order = []
for _ in range(T):
    t, x, y = map(int, input().rstrip().split())
    order.append((t, x, y))

ans = [P]
order.sort()
sick_list = [0] * (N + 1)
sick_list[P] = K
for at, ax, ay in order:
    if ax in ans and sick_list[ax] > 0:
        sick_list[ax] -= 1
        if ay not in ans:
            ans.append(ay)
            sick_list[ay] = K
    if ay in ans and sick_list[ay] > 0:
        sick_list[ay] -= 1
        if ax not in ans:
            ans.append(ax)
            sick_list[ax] = K

for i in range(1, N + 1):
    if i in ans:
        print(1, end="")
    else:
        print(0, end="")