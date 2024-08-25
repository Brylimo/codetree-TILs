# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

# 사람이 살고 있는 곳이 나오면
# 와이파이를 해당 위치로부터 오른쪽으로 m만큼 떨어진 곳에 놓은 뒤,
# 2m만큼 떨어진 곳에서 시작하여 다시 탐색을 진행합니다.
cnt, i = 0, 0
while i < n:
    if arr[i] == 1:
        cnt += 1
        i += 2 * m + 1
    else:
        i += 1

print(cnt)