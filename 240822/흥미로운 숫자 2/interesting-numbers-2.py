from collections import Counter
x, y = map(int, input().split())

ans = 0
for i in range(x, y + 1):
    digits = list(map(int, list(str(i))))

    counter = Counter(digits)

    if len(counter) == 2 and 1 in counter.values():
        ans += 1

print(ans)