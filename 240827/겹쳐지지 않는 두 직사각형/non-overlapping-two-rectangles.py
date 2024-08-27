import sys

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

ans = -sys.maxsize
for i in range(n):
    for j in range(m):
        for a in range(n):
            for b in range(m):
                for k in range(1, n + 1):
                    for l in range(1, m + 1):
                        for c in range(1, n + 1):
                            for d in range(1, m + 1):
                                if i == a and j == b:
                                    continue

                                if i + k - 1 < a or j + l - 1 < b or a + c - 1 < i or b + d - 1 < j:
                                    if i + k > n or a + c > n or j + l > m or b + d > m:
                                        continue

                                    first = sum([
                                        grid[x][y]
                                        for x in range(i, i + k)
                                        for y in range(j, j + l)
                                    ])

                                    second = sum([
                                        grid[x][y]
                                        for x in range(a, a + c)
                                        for y in range(b, b + d)
                                    ])
                                    
                                    ans = max(ans, first + second)

print(ans)