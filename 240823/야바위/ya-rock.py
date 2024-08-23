n = int(input())

games = []
for _ in range(n):
    a, b, c = map(int, input().split())
    games.append((a, b, c))

ans = 1
total = 0
score = 0
for i in range(1, 4):    
    stones = [0] * 4
    stones[i] = 1
    for j in range(n):
        a, b, c = games[j]

        stones[a], stones[b] = stones[b], stones[a]

        if stones[c] == 1:
            score+=1

    if total < score:
        total = score
        ans = i 

print(ans)