from copy import deepcopy
import sys

array = list(map(int, input().split()))

for i in range(1, 41):
    for j in range(i, 41):
        for k in range(j, 41):
            for l in range(k, 41):
                a, b, c, d = i, j, k, l

                varray = deepcopy(array)
                if a not in varray:
                    continue
                
                varray.remove(a)
                if b not in varray:
                    continue
                    
                varray.remove(b)
                if c not in varray:
                    continue

                varray.remove(c)
                if d not in varray:
                    continue

                varray.remove(d)
                if a + b not in varray:
                    continue

                varray.remove(a + b)
                if b + c not in varray:
                    continue
                
                varray.remove(b + c)
                if c + d not in varray:
                    continue

                varray.remove(c + d)
                if d + a not in varray:
                    continue

                varray.remove(d + a)
                if a + c not in varray:
                    continue

                varray.remove(a + c)
                if b + d not in varray:
                    continue

                varray.remove(b + d)
                if a + b + c not in varray:
                    continue

                varray.remove(a + b + c)
                if a + b + d not in varray:
                    continue

                varray.remove(a + b + d)
                if a + c + d not in varray:
                    continue

                varray.remove(a + c + d)
                if b + c + d not in varray:
                    continue

                varray.remove(b + c + d)
                if a + b + c + d not in varray:
                    continue

                varray.remove(a + b + c + d)
                print(a, b, c, d)
                sys.exit(0)