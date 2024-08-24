n = int(input())

birds = [-1] * 11
cnt = 0
for _ in range(n):
    bird, loc = map(int, input().split())

    if birds[bird] == -1:
        birds[bird] = loc
    elif birds[bird] != loc:
        cnt += 1

print(cnt)