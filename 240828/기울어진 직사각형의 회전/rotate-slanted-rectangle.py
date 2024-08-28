n = int(input())
a = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

def rotate(r, c, m1, m2, m3, m4, dir):
    dx = [-1, -1, 1, 1]
    dy = [1, -1, -1, 1]

    temp = a[r][c]
    s_cnt = [m1, m2, m3, m4]

    x, y = r, c
    if dir == 0:
        for i in range(4, 0, -1):
            while s_cnt[i - 1] > 0:
                nx = x - dx[i - 1]
                ny = y - dy[i - 1]

                s_cnt[i - 1] -= 1

                a[x][y] = a[nx][ny]
                x, y = nx, ny

        a[r - 1][c + 1] = temp
    elif dir == 1:
        for i in range(4):
            while s_cnt[i] > 0:
                nx = x + dx[i]
                ny = y + dy[i]

                s_cnt[i] -= 1

                a[x][y] = a[nx][ny]
                x, y = nx, ny

        a[r - 1][c - 1] = temp

for row in range(1, n + 1):
    given_nums = list(map(int, input().split()))
    for col, num in enumerate(given_nums, start = 1):
        a[row][col] = num

r, c, m1, m2, m3, m4, dir = map(int, input().split())

rotate(r, c, m1, m2, m3, m4, dir)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(a[i][j], end=" ")
    print()