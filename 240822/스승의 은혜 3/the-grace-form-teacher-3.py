class Present:
    def __init__(self, p, s):
        self.p = p 
        self.s = s

n, b = map(int, input().split())

presents = []
for _ in range(n):
    p, s = map(int, input().split())
    presents.append(Present(p, s))

presents.sort(key=lambda a:(a.p + a.s, -a.p))

ans = 0

for i in range(n):
    cnt = 0
    sum_value = 0
    
    sum_value += presents[i].p // 2 + presents[i].s
    cnt += 1

    for j in range(n):
        if i == j:
            continue

        sum_value += presents[j].p + presents[j].s 
        if sum_value > b:
            break
        cnt += 1

    ans = max(ans, cnt)

print(ans)