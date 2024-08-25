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
                    idx = j
                    while idx >= 0 and array[i] != alphas[i]:
                        array[idx], array[idx - 1] = array[idx - 1], array[idx]
                        idx -= 1
                        cnt += 1
                else:
                    while idx < n and array[i] != alphas[i]:
                        array[idx], array[idx + 1] = array[idx + 1], array[idx]
                        idx += 1
                        cnt += 1
                break

print(cnt)