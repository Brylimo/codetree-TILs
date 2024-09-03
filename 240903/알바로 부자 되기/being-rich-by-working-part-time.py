n = int(input())

chores = []
dp = [0] * n

for _ in range(n):
    s, e, p = map(int, input().split())
    chores.append((s, e, p))

chores.sort()

for i in range(n):
    dp[i] = chores[i][2]

    for j in range(i):
        si, ei, pi = chores[i]
        sj, ej, pj = chores[j]


        # 두 알바가 겹치지 않음
        if ej < si:
            dp[i] = max(dp[i], dp[j] + pi)

ans = max(dp)
print(ans)