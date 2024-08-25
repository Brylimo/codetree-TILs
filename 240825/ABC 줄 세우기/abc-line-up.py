import sys

n = int(input())
array = list(input().split())

alphas = []
for i in range(n):
    alphas.append(chr(ord('A') + i))

cnt = 0
if alphas == array:
    print(cnt)
    sys.exit(0)

for i in range(n):
    if array[i] != alphas[i]:
        for j in range(n):
            if array[j] == alphas[i]:
                if j > i:
                    while array[i] != alphas[i]:
                        array[j], array[j - 1] = array[j - 1], array[j]
                        cnt += 1
                        break
                else:
                    while array[i] != alphas[i]:
                        array[j], array[j + 1] = array[j + 1], array[j]
                        cnt += 1
                        break

print(cnt)