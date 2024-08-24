a, b, c = map(int, input().split())

# aight
if b == a + 1 and c == b + 1:
    print(0)
elif c == b + 2 or b == a + 2:
    print(1)
else:
    print(2)