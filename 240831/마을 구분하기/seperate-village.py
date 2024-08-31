n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]

people = 0
def dfs(x, y):
    global people

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    people += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if not visited[nx][ny] and grid[nx][ny] == 1:
            visited[nx][ny] = True
            dfs(nx, ny)

village_cnt = 0
people_list = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            dfs(i, j)
            people_list.append(people)
            village_cnt += 1
            people = 0

people_list.sort()
print(village_cnt)
for p in people_list:
    print(p)