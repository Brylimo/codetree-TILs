k, n = map(int, input().split())

contests = []
for _ in range(k):
    contests.append(list(map(int, input().split())))

cnt = 0

# i번째 개발자 기준
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if i == j:
            continue

        times1= [0] * k
        times2 = [0] * k
        for e in range(k):
            for t in range(n):
                if contests[e][t] == i:
                    times1[e] = t 
                elif contests[e][t] == j:
                    times2[e] = t

        a_cnt = 0
        b_cnt = 0
        for u in range(k):
            if times1[u] < times2[u]:
                a_cnt += 1
            else:
                b_cnt += 1

        if a_cnt == k or b_cnt == k:
            cnt += 1
    
print(cnt)