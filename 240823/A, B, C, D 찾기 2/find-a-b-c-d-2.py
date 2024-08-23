import sys

array = list(map(int, input().split()))

for i in range(1, 41):
    for j in range(i, 41):
        for k in range(j, 41):
            for l in range(k, 41):
                a, b, c, d = i, j, k, l

                if a not in array:
                    continue
                
                if b not in array:
                    continue

                if c not in array:
                    continue

                if d not in array:
                    continue

                if a + b not in array:
                    continue

                if b + c not in array:
                    continue
                
                if c + d not in array:
                    continue

                if d + a not in array:
                    continue

                if a + c not in array:
                    continue

                if b + d not in array:
                    continue

                if a + b + c not in array:
                    continue

                if a + b + d not in array:
                    continue

                if a + c + d not in array:
                    continue

                if b + c + d not in array:
                    continue

                if a + b + c + d not in array:
                    continue

                print(a, b, c, d)
                sys.exit(0)