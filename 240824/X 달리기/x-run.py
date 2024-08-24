x = int(input())
half = x // 2

velo = 1
dist = 0
ans = 0
prev = 0
for i in range(1, x + 1):
    dist += velo

    if dist >= x and velo == 1:
        ans = i
        break

    if dist + dist < x:
        velo += 1
    elif dist + prev < x:
        pass
    else:
        if velo > 1:
            velo -= 1

    prev = dist    
    
print(ans)