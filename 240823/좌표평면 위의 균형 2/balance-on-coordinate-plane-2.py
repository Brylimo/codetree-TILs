import sys
n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = sys.maxsize
for i in range(101):
    for j in range(101):
        if i % 2 == 1 or j % 2 == 1:
            continue

        regions = [0] * 4
        # x > 0 & y > 0
        for x, y in points:
            if x > i and y > j:
                regions[0] += 1
        # x > 0 & y < 0
        for x, y in points:
            if x > i and y < j:
                regions[1] +=1
        # x < 0 & y < 0
        for x, y in points:
            if x < i and y < j:
                regions[2] +=1
        # x < 0 & y > 0 
        for x, y in points:
            if x < i and y > j:
                regions[3] +=1

        max_cnt = max(regions)
        ans = min(ans, max_cnt)

print(ans)