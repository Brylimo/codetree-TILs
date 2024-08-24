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

            rsp = [i, j, k]

            victory = 0
            for u in range(n):
                r1, r2 = seq[u]

                if r1 == 1 and r2 == 3:
                    victory += 1
                elif r1 == 2 and r2 == 1:
                    victory += 1
                elif r1 == 3 and r2 == 2:
                    victory += 1

                ans = max(ans, victory)

print(ans)