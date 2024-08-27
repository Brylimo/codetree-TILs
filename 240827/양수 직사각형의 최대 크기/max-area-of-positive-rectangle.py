n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

def is_possible(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if grid[i][j] <= 0:
                return False

    return True

ans = -1
for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                if is_possible(i, j, k, l):
                    ans = max(ans, abs(k - i + 1) * abs(l - j + 1))

print(ans)