grid = []
for _ in range(3):
    grid.append(list(map(int, list(input()))))

ans = 0
for i in range(1, 10):
    for j in range(i + 1, 10):
        visited = [[0] * 3 for _ in range(3)]
        for a in range(3):
            for b in range(3):
                if grid[a][b] == i:
                    visited[a][b] = 1
                elif grid[a][b] == j:
                    visited[a][b] = 2

        cnt = 0
        for a in range(3):
            if visited[a][0] > 0 and visited[a][1] > 0 and visited[a][2] > 0 and 1 in visited[a] and 2 in visited[a]:
                cnt += 1
                break
            if visited[0][a] > 0 and visited[1][a] > 0 and visited[2][a] > 0 and 1 in [visited[0][a], visited[1][a], visited[2][a]] and 2 in [visited[0][a], visited[1][a], visited[2][a]]:
                cnt += 1
                break
        
        if visited[0][0] > 0 and visited[1][1] > 0 and visited[2][2] > 0 and 1 in [visited[0][0], visited[1][1], visited[2][2]] and 2 in [visited[0][0], visited[1][1], visited[2][2]]:
            cnt += 1
        if visited[0][2] > 0 and visited[1][1] > 0 and visited[2][0] > 0 and 1 in [visited[0][2], visited[1][1], visited[2][0]] and 2 in [visited[0][2], visited[1][1], visited[2][0]]:
            cnt += 1

        if cnt > 0:
            ans += 1

print(ans)