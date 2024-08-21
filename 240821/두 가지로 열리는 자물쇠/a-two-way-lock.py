# 변수 선언 및 입력
n = int(input())
a, b, c = tuple(map(int, input().split()))
a2, b2, c2 = tuple(map(int, input().split()))


# 모든 조합을 다 만들어 봅니다.
cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            # 모든 자리가 주어진 첫 조합과의 거리가 2 이내인지 확인합니다.
            if (abs(a - i) <= 2 or abs(a - i) >= n - 2) and (abs(b - j) <= 2 or abs(b - j) >= n - 2) and \
               (abs(c - k) <= 2 or abs(c - k) >= n - 2):
                cnt += 1
			
			# 모든 자리가 주어진 두 번째 조합과의 거리가 2 이내인지 확인합니다.
            elif (abs(a2 - i) <= 2 or abs(a2 - i) >= n - 2) and (abs(b2 - j) <= 2 or abs(b2 - j) >= n - 2) and \
               (abs(c2 - k) <= 2 or abs(c2 - k) >= n - 2):
                cnt += 1

print(cnt)