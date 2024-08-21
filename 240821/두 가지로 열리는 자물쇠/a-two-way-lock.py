n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

feasible_a1 = [a1, (1 if (a1 + 1) % (n+1) == 0 else (a1 + 1) % (n+1)), (1 if (a1 + 2) % (n+1) == 0 else (a1 + 2) % (n+1)), (n + a1 - 1 if a1 - 1 <= 0 else a1 - 1), (n + a1 - 2 if a1 - 2 <= 0 else a1 - 2)]
feasible_b1 = [b1, (1 if (b1 + 1) % (n+1) == 0 else (b1 + 1) % (n+1)), (1 if (b1 + 2) % (n+1) == 0 else (b1 + 1) % (n+1)), (n + b1 - 1 if b1 - 1 <= 0 else b1 - 1), (n + b1 - 2 if b1 - 2 <= 0 else b1 - 2)]
feasible_c1 = [c1, (1 if (c1 + 1) % (n+1) == 0 else (c1 + 1) % (n+1)), (1 if (c1 + 2) % (n+1) == 0 else (c1 + 2) % (n+1)), (n + c1 - 1 if c1 - 1 <= 0 else c1 - 1), (n + c1 - 2 if c1 - 2 <= 0 else c1 - 2)]

feasible_a2 = [a2, (1 if (a2 + 1) % (n+1) == 0 else (a2 + 1) % (n+1)), (1 if (a2 + 2) % (n+1) == 0 else (a2 + 2) % (n+1)), (n + a2 - 1 if a2 - 1 <= 0 else a2 - 1), (n + a2 - 2 if a2 - 2 <= 0 else a2 - 2)]
feasible_b2 = [b2, (1 if (b2 + 1) % (n+1) == 0 else (b2 + 1) % (n+1)), (1 if (b2 + 2) % (n+1) == 0 else (b2 + 2) % (n+1)), (n + b2 - 1 if b2 - 1 <= 0 else b2 - 1), (n + b2 - 2 if b2 - 2 <= 0 else b2 - 2)]
feasible_c2 = [c2, (1 if (c2 + 1) % (n+1) == 0 else (c2 + 1) % (n+1)), (1 if (c2 + 2) % (n+1) == 0 else (c2 + 2) % (n+1)), (n + c2 - 1 if c2 - 1 <= 0 else c2 - 1), (n + c2 - 2 if c2 - 2 <= 0 else c2 - 2)]

cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if (i in feasible_a1 and j in feasible_b1 and k in feasible_c1) or (i in feasible_a2 and j in feasible_b2 and k in feasible_c2):
                cnt += 1
                
print(cnt)