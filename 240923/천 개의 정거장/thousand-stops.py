INF = (10**17) + 1

# 변수 선언 및 입력:
m = 1000 # 서로 다른 정점의 수
a, b, n = tuple(map(int, input().split()))
graph = [
    [(INF, 0)] * (m + 1)         # (비용, 시간)을 기록
    for _ in range(m + 1)
]
dist = [(INF, 0)] * (m + 1)      # (비용, 시간)을 기록
visited = [False] * (m + 1)

for i in range(1, m + 1):
    # 자기 자신은 비용과 시간이 전혀 소요되지 않음
    graph[i][i] = (0, 0)

# 그래프를 인접행렬로 표현
for _ in range(n):
    cost, stop_num = tuple(map(int, input().split()))
    
    stops = list(map(int, input().split()))

    for i in range(stop_num):
        for j in range(i + 1, stop_num):
            graph[stops[i]][stops[j]] = min(graph[stops[i]][stops[j]],
                                            (cost, j - i))

# 시작위치에는 dist값을 0으로 설정
dist[a] = (0, 0)

# O(|V|^2) 다익스트라 코드
for _ in range(m):
    # V개의 정점 중 
    # 아직 방문하지 않은 정점 중
    # dist값이 가장 작은 정점을 찾아줍니다.
    min_index = -1
    for i in range(1, m + 1):
        if visited[i]:
            continue
        
        if min_index == -1 or dist[min_index] > dist[i]:
            min_index = i

    # 최솟값에 해당하는 정점에 방문 표시를 진행합니다.
    visited[min_index] = True
    min_cost, min_time = dist[min_index]

    # 최솟값에 해당하는 정점에 연결된 간선들을 보며
    # 시작점으로부터의 최단거리 값을 갱신해줍니다.
    for i in range(1, m + 1):
        cost, time = graph[min_index][i]
        dist[i] = min(dist[i], (min_cost + cost, min_time + time))

# 만약 도달이 불가능하다면 -1 -1이 답이 됩니다.
if dist[b] == (INF, 0):
    dist[b] = (-1, -1)

min_cost, min_time = dist[b]
print(min_cost, min_time)