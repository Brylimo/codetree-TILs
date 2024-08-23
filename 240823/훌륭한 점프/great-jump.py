n, k = map(int, input().split())
array = list(map(int, input().split()))

def is_possible(target):
    reasonable = []
    for j in range(n):
        if array[j] <= target:
            reasonable.append(j)

    for i in range(len(reasonable) - 1):
        if abs(reasonable[i] - reasonable[i + 1]) > k:
            return False

    return True

ans = int(1e9)
for i in range(max(array), 0, -1):
    if is_possible(i):
        ans = min(ans, i)
    else:
        break

print(ans)