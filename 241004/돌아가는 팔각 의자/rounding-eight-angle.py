m = 4

chairs = [[0]]

left = [0] * (m + 1)
right = [0] * (m + 1)
visited = [False] * (m + 1)
for i in range(m):
    chairs.append(list(map(int, list(input()))))

k = int(input())

def rotate(n, d):
    if visited[n]:
        return

    visited[n] = True

    if d == 1: # 시계 방향
        temp = chairs[n].pop()
        chairs[n].insert(0, temp)
    else: # 반시계 방향
        temp = chairs[n].pop(0)
        chairs[n].append(temp)

    # 왼쪽 확인
    if n - 1 > 0 and right[n - 1] != left[n]:
        if not visited[n - 1]:
            rotate(n - 1, -d)
    # 오른쪽 확인
    if n + 1 <= m and right[n] != left[n + 1]:
        if not visited[n + 1]:
            rotate(n + 1, -d)

    left[n] = chairs[n][6]
    right[n] = chairs[n][2]

# 왼쪽, 오른쪽 사람 초기화
for i in range(1, m + 1):
    left[i] = chairs[i][6]
    right[i] = chairs[i][2]

for _ in range(k):
    n, d = map(int, input().split())

    for i in range(1, m + 1):
        visited[i] = False

    rotate(n, d)

s1, s2, s3, s4 = chairs[1][0], chairs[2][0], chairs[3][0], chairs[4][0]

print(s1 + 2 * s2 + 4 * s3 + 8 * s4)