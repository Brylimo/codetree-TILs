n, m, p = map(int, input().split())

talks = []

overall = []
for i in range(n):
    overall.append(chr(ord('A') + i))
    
for _ in range(m):
    c, u = input().split()
    u = int(u)

    talks.append((c, u))

people = [[] for _ in range(n)]
lasts = []
for i in range(m, 0, -1):
    c, u = talks[i - 1]

    if u == 0:
        for alpha in overall:
            people[i - 1].append(alpha)
            lasts.append(alpha)
            continue

    people[i - 1].append(c)
    for j in range(len(lasts)):
        people[i - 1].append(lasts[j])

    lasts.append(c)

overall = set(overall)
target = set(people[p - 1])

ans = overall - target
for alpha in ans:
    print(alpha, end=" ")