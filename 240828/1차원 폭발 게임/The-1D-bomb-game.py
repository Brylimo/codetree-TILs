n, m = map(int, input().split())

bombs = []
for _ in range(n):
    bombs.append(int(input()))

def is_not_done():
    return any([
        bombs[i] == bombs[i + 1]
        for i in range(n - 1)
        if bombs[i] != 0
    ])

length = 0
while is_not_done():
    cnt = 1
    cur = 0
    for i in range(1, n):
        if bombs[cur] == bombs[i]:
            cnt += 1
        else:
            if cnt >= m:
                for j in range(cur, i):
                    bombs[j] = 0
            
            cur = i
            cnt = 1

    end_of_temp = 0
    temp = [0] * n
    for i in range(n):
        if bombs[i] != 0:
            temp[end_of_temp] = bombs[i]
            end_of_temp += 1

    length = end_of_temp
    for i in range(n):
        bombs[i] = temp[i]


print(length)
for i in range(n):
    if bombs[i] == 0:
        break
    else:
        print(bombs[i])