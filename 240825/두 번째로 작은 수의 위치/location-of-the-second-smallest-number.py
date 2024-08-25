import sys

n = int(input())
array = list(map(int, input().split()))

ref = sorted(array)
min_val = min(ref)

idx = -1
for i in range(n):
    if ref[i] != min_val:
        idx = i
        break

if idx == -1:
    print(-1)
    sys.exit(0)

if idx + 1 < n and ref[idx] == ref[idx + 1]:
    print(-1)
    sys.exit(0)
else:
    target = ref[idx]

    index = -2
    for i in range(n):
        if target == array[i]:
            index = i
            break

    print(index + 1)