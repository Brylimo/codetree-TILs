import sys

a, b, x, y = map(int, input().split())

ans = sys.maxsize
# case 1 a -> b
ans = min(ans, abs(b - a))

# case 2 a -> x -> y -> b
dist = abs(x - a) + abs(b - y)
ans = min(ans, dist)

# case 3 a -> y -> x -> b
dist = abs(y - a) + abs(b - x)
ans = min(ans, dist)

print(ans)