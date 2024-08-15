import sys
from copy import deepcopy
input = sys.stdin.readline


n = int(input().rstrip())
graph = []

boom_points = []
for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))
    for j in range(n):
        if graph[i][j] == 1:
            boom_points.append((i, j))

answer = 0
def explosion(curr_point):
    global graph, answer
    if curr_point == len(boom_points):
        cnt = 0
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 2:
                    cnt += 1
        answer = max(answer, cnt)
        return

    x, y = boom_points[curr_point]
    for k in range(3):
        vgraph = deepcopy(graph)
        if k == 0:
            if 0<= x-2 < n and graph[x - 2][y] == 0:
                graph[x - 2][y] = 2
            if 0<= x-1 < n and graph[x - 1][y] == 0:
                graph[x - 1][y] = 2
            if 0<= x+1 < n and graph[x + 1][y] == 0:
                graph[x + 1][y] = 2
            if 0<= x+2 < n and graph[x + 2][y] == 0:
                graph[x + 2][y] = 2
        elif k == 1:
            if 0<= x-1 < n and graph[x - 1][y] == 0:
                graph[x - 1][y] = 2
            if 0<= x+1 < n and graph[x + 1][y] == 0:
                graph[x + 1][y] = 2
            if 0<= y-1 < n and graph[x][y-1] == 0:
                graph[x][y-1] = 2
            if 0<= y+1 < n and graph[x][y + 1] == 0:
                graph[x][y + 1] = 2
        elif k == 2:
            if 0<= x-1 < n and 0 <= y - 1 < n and graph[x - 1][y - 1] == 0:
                graph[x - 1][y - 1] = 2
            if 0<= x-1 < n and 0 <= y + 1 < n and graph[x - 1][y + 1] == 0:
                graph[x - 1][y + 1] = 2
            if 0<= x+1 < n and 0 <= y - 1 < n and graph[x+1][y-1] == 0:
                graph[x+1][y-1] = 2
            if 0<= x+1 < n and 0 <= y + 1 < n and graph[x + 1][y + 1] == 0:
                graph[x + 1][y + 1] = 2

        explosion(curr_point + 1)

        graph = vgraph

explosion(0)
print(answer + len(boom_points))