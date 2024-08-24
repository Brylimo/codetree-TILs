n = int(input())

seq = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    seq.append((x1, x2))

ans = 0
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i == j or i == k or j == k:
                continue

            rsp = [i + 1, j + 1, k + 1]

            victory = 0
            for u in range(n):
                r1, r2 = seq[u]

                if rsp[r1 - 1] == 1 and rsp[r2 - 1] == 3:
                    victory += 1
                elif rsp[r1 - 1] == 2 and rsp[r2 - 1] == 1:
                    victory += 1
                elif rsp[r1 - 1] == 3 and rsp[r2 - 1] == 2:
                    victory += 1

            ans = max(ans, victory)

print(ans)