n = int(input())
array = list(input().split())

alphas = []
for i in range(n):
    alphas.append(chr(ord('A') + i))

cnt = 0
for i in range(n):
    if array[i] != alphas[i]:
        for j in range(n):
            if array[j] == alphas[i]:
                array[i], array[j] = array[j], array[i]
                cnt += 1
                break

print(cnt)