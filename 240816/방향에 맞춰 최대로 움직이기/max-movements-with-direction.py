# 변수 선언 및 입력:
n = int(input())
num = [
    list(map(int, input().split()))
    for _ in range(n)
]
move_dir = [
    list(map(int, input().split()))
    for _ in range(n)
]

ans = 0


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x, y, prev_num):
    return in_range(x, y) and num[x][y] > prev_num


def find_max(x, y, cnt):
    global ans
    
    # 언제 끝날지 모르기 때문에
    # 항상 최댓값을 갱신해줍니다.
    ans = max(ans, cnt)
    
    dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
    dys = [0, 1, 1, 1, 0, -1, -1, -1]
    
    d = move_dir[x][y] - 1
    
    for i in range(n):
        nx, ny = x + dxs[d] * i, y + dys[d] * i
        if can_go(nx, ny, num[x][y]):
            find_max(nx, ny, cnt + 1)

            
r, c = tuple(map(int, input().split()))

find_max(r - 1, c - 1, 0)
print(ans)