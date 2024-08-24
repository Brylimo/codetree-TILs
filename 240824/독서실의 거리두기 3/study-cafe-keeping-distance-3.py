n = int(input())
seats = list(map(int, list(input())))

dist = []
cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if seats[i] == 1 and seats[j] == 1:
            dist.append(j - i - 1)
            break

dist.sort(reverse=True)

if dist[0] == dist[1]:
    dist.pop()
    dist.append(dist[0] - 1)
else:
    temp = dist.pop()
    dist.append(temp - 1)

for i in range(n):
    for j in range(i + 1, n):
        if seats[i] == 1 and seats[j] == 1:
            dist.append(j - i - 1)
            break

dist.sort()
print(dist[0])