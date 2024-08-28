from collections import deque

n, m, q = map(int, input().split())

buildings = []
for _ in range(n):
    buildings.append(list(map(int, input().split())))

queue = deque([])
visited = [False] * n
for i in range(q):
    r, d = input().split()
    r = int(r)

    queue.append((r, d, None))

while queue:
    ar, ad, afrom = queue.popleft()

    if ad == 'L':
        temp = buildings[ar - 1][-1]
        for i in range(m - 1, 0, -1):
            buildings[ar - 1][i] = buildings[ar - 1][i - 1]
        
        buildings[ar - 1][0] = temp

        next_ad = 'R'
    elif ad == 'R':
        temp = buildings[ar - 1][0]
        for i in range(m-1):
            buildings[ar - 1][i] = buildings[ar - 1][i + 1]

        buildings[ar - 1][-1] = temp
        
        next_ad = 'L'

    if ar - 2 >= 0 and afrom != ar - 2:
        for j in range(m):
            if buildings[ar - 1][j] == buildings[ar - 2][j]:
                queue.append((ar - 1, next_ad, ar - 1))
                break
    if ar < n and afrom != ar:
        for j in range(m):
            if buildings[ar - 1][j] == buildings[ar][j]:
                queue.append((ar + 1, next_ad, ar - 1))
                break

for i in range(n):
    for j in range(m):
        print(buildings[i][j], end=" ")
    print()