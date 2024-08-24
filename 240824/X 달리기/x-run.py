x = int(input())
half = x // 2

velo = 1
dist = 0
ans = 0
for i in range(1, x + 1):
    dist += velo

    if dist >= x:
        ans = i
        break

    if dist <= half:
        velo += 1
    else:
        if velo > 1:
            velo -= 1    
    
print(ans)