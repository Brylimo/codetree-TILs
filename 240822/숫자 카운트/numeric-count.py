n = int(input())

ops = []
for _ in range(n):
    num, cnt1, cnt2 = input().split()
    ops.append((list(map(int, list(num))), int(cnt1), int(cnt2)))

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or i == k or j == k:
                continue

            target = [i, j, k]

            correct = 0
            for digits, cnt1, cnt2 in ops:
                temp_cnt1 = 0
                temp_cnt2 = 0
                
                if i == digits[0]:
                    temp_cnt1 += 1
                if j == digits[1]:
                    temp_cnt1 += 1
                if k == digits[2]:
                    temp_cnt1 += 1

                if i in digits:
                    temp_cnt2 += 1
                if i != j and j in digits:
                    temp_cnt2 += 1
                if i != k and j != k and k in digits:
                    temp_cnt2 += 1

                temp_cnt2 -= temp_cnt1
                if cnt1 == temp_cnt1 and cnt2 == temp_cnt2:
                    correct += 1

            if correct == n:
                ans += 1
            
print(ans)