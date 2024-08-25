n, m = map(int, input().split())
array = list(map(int, input().split()))

ans = 0
cnt = 0
total = sum(array)
while True:
    loc = None
    max_cnt = 0
    block_size = min(2*m + 1, n)
    for i in range(n - block_size + 1):
        overlap = 0
        for j in range(block_size):
            if array[i + j] == 1:
                overlap += 1

        if max_cnt < overlap:
            max_cnt = overlap
            loc = i

    cnt += max_cnt
    if cnt != total:
        ans += 1
        if loc is not None:
            for i in range(block_size):
                array[loc + i] = 0
    else:
        ans += 1
        break

print(ans)