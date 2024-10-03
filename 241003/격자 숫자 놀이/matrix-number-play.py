r, c, k = map(int, input().split())
r, c = r - 1, c - 1

grid = [
    list(map(int, input().split()))
    for _ in range(3)
]

elapsed_time = 0
def end():
    if elapsed_time > 100:
        return True

    if len(grid) > r and len(grid[r]) > c and grid[r][c] == k:
        return True

    return False

def get_next_idx(arr, idx):
    cnt = 1
    j = -1

    for i in range(idx + 1, len(arr)):
        if arr[i] != arr[idx]:
            j = i
            break
        cnt += 1

    return (j, cnt)
def process():
    global grid

    # 행, 열 개수 비교
    row_cnt = len(grid)
    column_cnt = len(grid[0])

    if row_cnt > 100:
        grid = grid[:100]
    if column_cnt > 100:
        grid = [arr[:100] for arr in grid]

    if row_cnt >= column_cnt:
        for i in range(row_cnt):
            temp = grid[i]
            temp.sort()
            tlst = []

            if len(temp) == 0:
                continue

            p = 0
            while p < column_cnt:
                num = temp[p]
                next_idx, count = get_next_idx(temp, p)
                p = next_idx

                tlst.append((count, num))

                if p == -1:
                    break

            tlst.sort()
            rlst = []
            for c, n in tlst:
                if n == 0:
                    continue

                rlst.append(n)
                rlst.append(c)

            grid[i] = rlst[:]

        max_col = max([len(grid[i]) for i in range(row_cnt)])
        for i in range(row_cnt):
            if len(grid[i]) < max_col:
                grid[i].extend([0] * (max_col - len(grid[i])))

    else:
        new_grid = []
        for i in range(column_cnt):
            temp = [arr[i] for arr in grid if arr[i] > 0]
            temp.sort()
            tlst = []

            if len(temp) == 0:
                continue

            p = 0
            while p < column_cnt:
                num = temp[p]
                next_idx, count = get_next_idx(temp, p)
                p = next_idx

                tlst.append((count, num))

                if p == -1:
                    break

            tlst.sort()
            rlst = []
            for c, n in tlst:
                rlst.append(n)
                rlst.append(c)

            new_grid += [rlst]

        max_col = max([len(new_grid[i]) for i in range(len(new_grid))])
        for i in range(len(new_grid)):
            if len(new_grid[i]) < max_col:
                new_grid[i].extend([0] * (max_col - len(new_grid[i])))
        temp = list(map(list, zip(*new_grid)))

        grid = temp[:]

while not end():
    # 과정 진행
    process()

    elapsed_time += 1

if elapsed_time > 100:
    print(-1)
else:
    print(elapsed_time)