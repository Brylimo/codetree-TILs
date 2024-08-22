n = int(input())

lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            line = [0] * 101
            for h in range(n):
                if h not in [i, j, k]:
                    a = lines[h][0]
                    b = lines[h][1]

                    for u in range(a, b + 1):
                        line[u] += 1

            correct = True
            for t in range(101):
                if line[t] > 1:
                    correct = False
                    break
            
            if correct:
                ans += 1

print(ans)